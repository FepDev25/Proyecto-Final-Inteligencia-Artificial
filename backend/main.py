# backend/main.py

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi.responses import StreamingResponse
from io import BytesIO
from explanation_service import generar_explicacion_gemini
from tts_service import generar_audio
from pydantic import BaseModel
from models import cargar_modelo, cargar_etiquetas, predecir_imagen_completa

MODEL_PATH = "./modelo/best_model.pth"
ETIQUETAS_PATH = "./modelo/clases.txt"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


modelo = cargar_modelo(MODEL_PATH)
etiquetas = cargar_etiquetas(ETIQUETAS_PATH)


@app.get("/")
def read_root():
    return {"message": "API de predicción de enfermedades de la piel"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Guardar imagen temporalmente
    file_location = f"./temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    diagnostico_nombre, prob, otras_condiciones, sintomas = predecir_imagen_completa(modelo, file_location, etiquetas)

    os.remove(file_location)

    explicacion_ia = generar_explicacion_gemini(diagnostico_nombre)

    nota_medica = "Nota importante: Este análisis es preliminar y no sustituye una evaluación médica profesional. Si los síntomas persisten o empeoran, busca atención médica."

    # Combina la explicación + nota
    resumen_completo = f"{explicacion_ia} {nota_medica}"

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


# Modelo del body
class TextRequest(BaseModel):
    text: str

@app.post("/tts")
async def text_to_speech(body: TextRequest):
    try:
        # Llama a la función que genera el audio
        audio_content = generar_audio(body.text)

        # Devuelve el audio como MP3
        audio_stream = BytesIO(audio_content)
        return StreamingResponse(audio_stream, media_type="audio/mpeg")
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})