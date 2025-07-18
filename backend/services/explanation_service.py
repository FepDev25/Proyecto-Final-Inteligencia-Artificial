import os
import google.generativeai as genai
import re

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./credentials/proyecto-final-465314-9a3fcd7e7957.json"

genai.configure()  


def limpiar_formato_markdown(texto: str) -> str:
    # Elimina **negritas**, *cursivas* y ## títulos
    texto = re.sub(r'\*\*(.*?)\*\*', r'\1', texto)  # **negrita**
    texto = re.sub(r'\*(.*?)\*', r'\1', texto)      # *cursiva*
    texto = re.sub(r'#+\s*(.*)', r'\1', texto)      # ## Título
    return texto.strip()


def generar_explicacion_gemini(diagnostico: str) -> str:
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")

        prompt = (
            f"Explícame de manera breve y sencilla qué es {diagnostico}, "
            "cuáles son sus posibles causas, y qué recomendaciones generales se deben seguir. "
            "Usa un lenguaje claro para pacientes sin conocimientos médicos. Solo responde el texto, sin formato markdown."
        )

        response = model.generate_content(prompt)

        texto_bruto = response.text.strip()
        return limpiar_formato_markdown(texto_bruto)

    except Exception as e:
        print(f"[Error Gemini AI] {e}")
        return f"{diagnostico} es una condición cutánea que debe ser evaluada por un dermatólogo. Evita la auto-medicación."
