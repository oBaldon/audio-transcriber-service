from fastapi import FastAPI, UploadFile, File, HTTPException
from services.whisper_service import transcribe_audio
from config.settings import Config
import os
import uvicorn
from utils.file_handler import save_upload_file

# Inicializar o aplicativo FastAPI
app = FastAPI(title="Audio Transcriber Service", version="1.0.0")

# Lista de tipos MIME suportados
SUPPORTED_AUDIO_TYPES = [
    "audio/wav",
    "audio/x-wav",
    "audio/mpeg",     # MP3
    "audio/x-flac",   # FLAC
    "audio/ogg",      # OGG
    "audio/webm",     # WebM
    "audio/mp4",      # M4A (MPEG-4 Audio)
    "audio/x-m4a"     # Outra variante do M4A
]


# Endpoint para upload e transcrição de áudio
@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    # Validar tipo de arquivo
    if file.content_type not in SUPPORTED_AUDIO_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"O arquivo enviado não é um áudio válido. Tipo recebido: {file.content_type}"
        )

    # Salvar o arquivo temporariamente
    saved_file_path = await save_upload_file(file)

    # Realizar a transcrição
    try:
        transcription = transcribe_audio(saved_file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao transcrever o áudio: {str(e)}")
    finally:
        # Remover o arquivo temporário após a transcrição
        if os.path.exists(saved_file_path):
            os.remove(saved_file_path)

    return {"transcription": transcription}

# Ponto de entrada principal
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=Config.APP_PORT, debug=Config.DEBUG)
