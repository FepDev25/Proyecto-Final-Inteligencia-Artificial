from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from sqlalchemy.orm import Session
from io import BytesIO
import os
from typing import List

from services.explanation_service import generar_explicacion_gemini
from services.tts_service import generar_audio
from services.prediction_service import cargar_modelo, cargar_etiquetas, predecir_imagen_completa
from models import schemas
from database import models
from database.connection import get_db

MODEL_PATH = "./modelo/best_model.pth"
ETIQUETAS_PATH = "./modelo/clases.txt"

router = APIRouter()

modelo = cargar_modelo(MODEL_PATH)
etiquetas = cargar_etiquetas(ETIQUETAS_PATH)

@router.get("/")
def read_root():
    return {"message": "API de predicción de enfermedades de la piel"}

@router.post("/predict")
async def predict(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = f"./temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    diagnostico_nombre, prob, otras_condiciones, sintomas = predecir_imagen_completa(modelo, file_location, etiquetas)

    os.remove(file_location)

    explicacion_ia = generar_explicacion_gemini(diagnostico_nombre)

    nota_medica = "Nota importante: Este análisis es preliminar y no sustituye una evaluación médica profesional. Si los síntomas persisten o empeoran, busca atención médica."

    resumen_completo = f"{explicacion_ia} {nota_medica}"

    # Guardar la predicción en la base de datos
    db_enfermedad = db.query(models.Enfermedad).filter(models.Enfermedad.nombre_enfermedad == diagnostico_nombre).first()
    id_enfermedad = db_enfermedad.id_enfermedad if db_enfermedad else None

    db_prediccion = models.Prediccion(
        id_enfermedad=id_enfermedad,
        url_imagen=file_location,
        resumen=resumen_completo,
        porcentaje_coincidencia=round(prob, 2)
    )
    db.add(db_prediccion)
    db.commit()
    db.refresh(db_prediccion)

    for condicion in otras_condiciones:
        db_posible_condicion = models.PosibleCondicion(
            id_prediccion=db_prediccion.id_prediccion,
            nombre_condicion=condicion['condicion'],
            nombre_interno=condicion['sigla'],
            porcentaje=condicion['probabilidad']
        )
        db.add(db_posible_condicion)
    db.commit()


    response = {
        "diagnostico_principal": {
            "condicion": diagnostico_nombre,
            "probabilidad": round(prob, 2),
            "resumen": f"Luego de la predicción, la imagen muestra características consistentes con {diagnostico_nombre}.",
            "nota": nota_medica,
            "texto_completo": resumen_completo,
            "sintomas": sintomas
        },
        "otras_posibles_condiciones": otras_condiciones
    }

    return JSONResponse(content=response)

@router.post("/tts")
async def text_to_speech(body: schemas.TextRequest):
    try:
        audio_content = generar_audio(body.text)
        audio_stream = BytesIO(audio_content)
        return StreamingResponse(audio_stream, media_type="audio/mpeg")
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# CRUD Endpoints for Enfermedades

@router.post("/enfermedades/", response_model=schemas.Enfermedad)
def create_enfermedad(enfermedad: schemas.EnfermedadCreate, db: Session = Depends(get_db)):
    db_enfermedad = models.Enfermedad(nombre_enfermedad=enfermedad.nombre_enfermedad, descripcion=enfermedad.descripcion)
    db.add(db_enfermedad)
    db.commit()
    db.refresh(db_enfermedad)
    return db_enfermedad

@router.get("/enfermedades/", response_model=List[schemas.Enfermedad])
def read_enfermedades(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    enfermedades = db.query(models.Enfermedad).offset(skip).limit(limit).all()
    return enfermedades

@router.get("/enfermedades/{enfermedad_id}", response_model=schemas.Enfermedad)
def read_enfermedad(enfermedad_id: int, db: Session = Depends(get_db)):
    db_enfermedad = db.query(models.Enfermedad).filter(models.Enfermedad.id_enfermedad == enfermedad_id).first()
    if db_enfermedad is None:
        raise HTTPException(status_code=404, detail="Enfermedad no encontrada")
    return db_enfermedad

@router.put("/enfermedades/{enfermedad_id}", response_model=schemas.Enfermedad)
def update_enfermedad(enfermedad_id: int, enfermedad: schemas.EnfermedadCreate, db: Session = Depends(get_db)):
    db_enfermedad = db.query(models.Enfermedad).filter(models.Enfermedad.id_enfermedad == enfermedad_id).first()
    if db_enfermedad is None:
        raise HTTPException(status_code=404, detail="Enfermedad no encontrada")
    db_enfermedad.nombre_enfermedad = enfermedad.nombre_enfermedad
    db_enfermedad.descripcion = enfermedad.descripcion
    db.commit()
    db.refresh(db_enfermedad)
    return db_enfermedad

@router.delete("/enfermedades/{enfermedad_id}", response_model=schemas.Enfermedad)
def delete_enfermedad(enfermedad_id: int, db: Session = Depends(get_db)):
    db_enfermedad = db.query(models.Enfermedad).filter(models.Enfermedad.id_enfermedad == enfermedad_id).first()
    if db_enfermedad is None:
        raise HTTPException(status_code=404, detail="Enfermedad no encontrada")
    db.delete(db_enfermedad)
    db.commit()
    return db_enfermedad

@router.get("/enfermedades/{enfermedad_id}/sintomas", response_model=List[schemas.Sintoma])
def read_sintomas_by_enfermedad(enfermedad_id: int, db: Session = Depends(get_db)):
    db_enfermedad = db.query(models.Enfermedad).filter(models.Enfermedad.id_enfermedad == enfermedad_id).first()
    if db_enfermedad is None:
        raise HTTPException(status_code=404, detail="Enfermedad no encontrada")
    
    sintomas = [enfermedad_sintoma.sintoma for enfermedad_sintoma in db_enfermedad.sintomas]
    return sintomas

# CRUD Endpoints for Predicciones

@router.post("/predicciones/", response_model=schemas.Prediccion)
def create_prediccion(prediccion: schemas.PrediccionCreate, db: Session = Depends(get_db)):
    db_prediccion = models.Prediccion(**prediccion.dict())
    db.add(db_prediccion)
    db.commit()
    db.refresh(db_prediccion)
    return db_prediccion

@router.get("/predicciones/", response_model=List[schemas.Prediccion])
def read_predicciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    predicciones = db.query(models.Prediccion).offset(skip).limit(limit).all()
    return predicciones

@router.get("/predicciones/{prediccion_id}", response_model=schemas.Prediccion)
def read_prediccion(prediccion_id: int, db: Session = Depends(get_db)):
    db_prediccion = db.query(models.Prediccion).filter(models.Prediccion.id_prediccion == prediccion_id).first()
    if db_prediccion is None:
        raise HTTPException(status_code=404, detail="Predicción no encontrada")
    return db_prediccion

@router.delete("/predicciones/{prediccion_id}", response_model=schemas.Prediccion)
def delete_prediccion(prediccion_id: int, db: Session = Depends(get_db)):
    db_prediccion = db.query(models.Prediccion).filter(models.Prediccion.id_prediccion == prediccion_id).first()
    if db_prediccion is None:
        raise HTTPException(status_code=404, detail="Predicción no encontrada")
    db.delete(db_prediccion)
    db.commit()
    return db_prediccion

# CRUD Endpoints for PosiblesCondiciones

@router.post("/posibles_condiciones/", response_model=schemas.PosibleCondicion)
def create_posible_condicion(posible_condicion: schemas.PosibleCondicionCreate, db: Session = Depends(get_db)):
    db_posible_condicion = models.PosibleCondicion(**posible_condicion.dict())
    db.add(db_posible_condicion)
    db.commit()
    db.refresh(db_posible_condicion)
    return db_posible_condicion

@router.get("/posibles_condiciones/", response_model=List[schemas.PosibleCondicion])
def read_posibles_condiciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posibles_condiciones = db.query(models.PosibleCondicion).offset(skip).limit(limit).all()
    return posibles_condiciones

@router.get("/posibles_condiciones/{posible_condicion_id}", response_model=schemas.PosibleCondicion)
def read_posible_condicion(posible_condicion_id: int, db: Session = Depends(get_db)):
    db_posible_condicion = db.query(models.PosibleCondicion).filter(models.PosibleCondicion.id_posible_condicion == posible_condicion_id).first()
    if db_posible_condicion is None:
        raise HTTPException(status_code=404, detail="Posible condicion no encontrada")
    return db_posible_condicion

@router.put("/posibles_condiciones/{posible_condicion_id}", response_model=schemas.PosibleCondicion)
def update_posible_condicion(posible_condicion_id: int, posible_condicion: schemas.PosibleCondicionCreate, db: Session = Depends(get_db)):
    db_posible_condicion = db.query(models.PosibleCondicion).filter(models.PosibleCondicion.id_posible_condicion == posible_condicion_id).first()
    if db_posible_condicion is None:
        raise HTTPException(status_code=404, detail="Posible condicion no encontrada")
    
    for key, value in posible_condicion.dict().items():
        setattr(db_posible_condicion, key, value)
        
    db.commit()
    db.refresh(db_posible_condicion)
    return db_posible_condicion

@router.delete("/posibles_condiciones/{posible_condicion_id}", response_model=schemas.PosibleCondicion)
def delete_posible_condicion(posible_condicion_id: int, db: Session = Depends(get_db)):
    db_posible_condicion = db.query(models.PosibleCondicion).filter(models.PosibleCondicion.id_posible_condicion == posible_condicion_id).first()
    if db_posible_condicion is None:
        raise HTTPException(status_code=404, detail="Posible condicion no encontrada")
    db.delete(db_posible_condicion)
    db.commit()
    return db_posible_condicion

@router.get("/predicciones/{prediccion_id}/posibles_condiciones", response_model=List[schemas.PosibleCondicion])
def read_posibles_condiciones_by_prediccion(prediccion_id: int, db: Session = Depends(get_db)):
    db_prediccion = db.query(models.Prediccion).filter(models.Prediccion.id_prediccion == prediccion_id).first()
    if db_prediccion is None:
        raise HTTPException(status_code=404, detail="Predicción no encontrada")
    
    return db_prediccion.posibles_condiciones
