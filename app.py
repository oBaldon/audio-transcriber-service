from fastapi import FastAPI, UploadFile, File, HTTPException
from services.whisper_service import transcribe_audio
from services.alignment_service import align_segments
from services.diarization_service import apply_diarization
from config.settings import Config
import os
import uvicorn
from utils.file_handler import save_upload_file, save_json_result, save_srt_result

app = FastAPI(title="Audio Transcriber Service", version="2.0")

SUPPORTED_AUDIO_TYPES = [
    "audio/wav", "audio/wave", "audio/x-wav", "audio/mpeg",
    "audio/x-flac", "audio/ogg", "audio/webm", "audio/mp4", "audio/x-m4a"
]

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    if file.content_type not in SUPPORTED_AUDIO_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Tipo de áudio inválido: {file.content_type}"
        )

    saved_file_path = await save_upload_file(file)

    try:
        # 1️⃣ Transcrição com Whisper puro
        transcription = transcribe_audio(saved_file_path)

        # 2️⃣ Alinhamento com WhisperX
        aligned_segments = align_segments(transcription["segments"], saved_file_path, transcription["language"])

        # 3️⃣ Diarização com WhisperX
        diarized_segments = apply_diarization(aligned_segments, saved_file_path)

        # 4️⃣ Salvar JSON e SRT localmente (mas não retornar paths na API)
        save_json_result({
            "language": transcription["language"],
            "text": transcription["text"],
            "segments": diarized_segments
        }, file.filename)

        save_srt_result(diarized_segments, file.filename)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao transcrever o áudio: {str(e)}")
    finally:
        if os.path.exists(saved_file_path):
            os.remove(saved_file_path)

    return {
        "language": transcription["language"],
        "text": transcription["text"],
        "segments": diarized_segments
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=Config.APP_PORT, reload=Config.DEBUG)
