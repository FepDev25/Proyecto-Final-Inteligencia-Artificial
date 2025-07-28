import torch
import torch.nn as nn
from PIL import Image
import torchvision.transforms as transforms
from sqlalchemy.orm import Session
from efficientnet_pytorch import EfficientNet
from google.cloud import storage
import os

def cargar_modelo(model_path):
    # Cargar checkpoint
    bucket_name = os.getenv('MODEL_BUCKET')
    if bucket_name:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        
        # Descargar modelo si no existe localmente
        local_model_path = f"./modelo/{os.path.basename(model_path)}"
        if not os.path.exists(local_model_path):
            blob = bucket.blob(os.path.basename(model_path))
            blob.download_to_filename(local_model_path)
            
        model_path = local_model_path

    checkpoint = torch.load(model_path, map_location=torch.device('cpu'), weights_only=False)
    num_classes = checkpoint['num_classes']
    
    # Reconstruir modelo EfficientNet-B3 con capa final personalizada
    modelo = EfficientNet.from_name('efficientnet-b3')
    in_features = modelo._fc.in_features
    modelo._fc = nn.Sequential(
        nn.Dropout(0.4),
        nn.Linear(in_features, num_classes)
    )
    
    # Cargar pesos del state_dict
    modelo.load_state_dict(checkpoint['model_state_dict'])
    modelo.eval()
    return modelo

def cargar_etiquetas(etiquetas_path):
    with open(etiquetas_path, "r", encoding='utf-8') as f:
        clases = [line.strip() for line in f.readlines()]
    return clases

def obtener_sintomas_desde_bd(nombre_enfermedad, db: Session):
    """Obtiene los síntomas de una enfermedad desde la base de datos"""
    from database import models
    
    enfermedad = db.query(models.Enfermedad).filter(
        models.Enfermedad.nombre_enfermedad == nombre_enfermedad
    ).first()
    
    if enfermedad:
        sintomas = [es.sintoma.nombre_sintoma for es in enfermedad.sintomas]
        return sintomas
    return []

# Función de predicción actualizada para trabajar con base de datos
def predecir_imagen_completa(modelo, ruta_img, etiquetas, db: Session = None, size=(224, 224)):
    transformaciones = transforms.Compose([
        transforms.Resize(size),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

    img = Image.open(ruta_img).convert('RGB')
    img_tensor = transformaciones(img).unsqueeze(0)

    with torch.no_grad():
        output = modelo(img_tensor)
        probs = torch.nn.functional.softmax(output[0], dim=0).numpy()

    # Diagnóstico principal
    idx_max = probs.argmax()
    nombre_max = etiquetas[idx_max]  # Ahora usamos directamente el nombre de la enfermedad
    probabilidad_max = float(probs[idx_max])

    # Obtener síntomas desde la base de datos
    sintomas = obtener_sintomas_desde_bd(nombre_max, db) if db else []

    # Otras condiciones
    otras_condiciones = []
    for idx, prob in enumerate(probs):
        if idx != idx_max:
            nombre_condicion = etiquetas[idx]
            otras_condiciones.append({
                "condicion": nombre_condicion,
                "sigla": nombre_condicion, 
                "probabilidad": round(float(prob), 2),
            })

    # Ordenar por probabilidad descendente
    otras_condiciones = sorted(otras_condiciones, key=lambda x: x["probabilidad"], reverse=True)

    return nombre_max, probabilidad_max, otras_condiciones, sintomas
