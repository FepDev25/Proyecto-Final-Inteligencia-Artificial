from google.cloud import texttospeech
import os

# Configura las credenciales
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./credentials/proyecto-final-465314-9a3fcd7e7957.json"

# Función que convierte texto en audio
def generar_audio(texto, idioma='es-US', genero='MALE'):
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=texto)

    voice = texttospeech.VoiceSelectionParams(
        language_code=idioma,
        ssml_gender=texttospeech.SsmlVoiceGender[genero]
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text,
        voice=voice,
        audio_config=audio_config
    )

    return response.audio_content
