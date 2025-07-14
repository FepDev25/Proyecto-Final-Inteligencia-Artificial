import torch
from PIL import Image
import torchvision.transforms as transforms

LESION_TYPE_DICT = {
    'akne': 'Acné',
    'benign': 'Lesión benigna',
    'ekzama': 'Eccema',
    'enfeksiyonel': 'Infección cutánea',
    'malign': 'Lesión maligna',
    'pigment': 'Lesión pigmentada no específica'
}

SINTOMAS = {
    'akne': ['Espinillas', 'Puntos negros', 'Granos inflamados'],
    'benign': ['Bultos suaves', 'Coloración uniforme', 'Crecimiento lento'],
    'ekzama': ['Enrojecimiento', 'Sequedad', 'Picazón', 'Ampollas'],
    'enfeksiyonel':['Ampollas', 'Pus', 'Enrojecimiento', 'Fiebre local'],
    'malign': ['Cambios de color', 'Bordes irregulares', 'Crecimiento rápido'],
    'pigment':['Manchas irregulares', 'Hiperpigmentación o despigmentación']
}

def cargar_modelo(model_path):
    modelo = torch.load(model_path, map_location=torch.device('cpu'), weights_only=False)
    modelo.eval()
    return modelo

def cargar_etiquetas(etiquetas_path):
    with open(etiquetas_path, "r") as f:
        clases = [line.strip() for line in f.readlines()]
    return clases

# Función de predicción
def predecir_imagen_completa(modelo, ruta_img, etiquetas, size=(224, 224)):
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
    sigla_max = etiquetas[idx_max]
    nombre_max = LESION_TYPE_DICT.get(sigla_max, sigla_max)
    probabilidad_max = float(probs[idx_max])

    # Sintomas como lista
    sintomas = SINTOMAS.get(sigla_max, [])

    # Otras condiciones
    otras_condiciones = []
    for idx, prob in enumerate(probs):
        if idx != idx_max:
            sigla = etiquetas[idx]
            nombre = LESION_TYPE_DICT.get(sigla, sigla)
            otras_condiciones.append({
                "condicion": nombre,
                "sigla": sigla,
                "probabilidad": round(float(prob), 2),
            })


    # Ordenar por probabilidad descendente
    otras_condiciones = sorted(otras_condiciones, key=lambda x: x["probabilidad"], reverse=True)

    return nombre_max, probabilidad_max, otras_condiciones, sintomas
