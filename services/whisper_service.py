import whisper
from config.settings import Config
from utils.device_utils import get_device

def transcribe_audio(audio_file_path: str) -> dict:
    """
    Transcreve o áudio com Whisper puro.
    Retorna: dict com 'language', 'text' e 'segments'
    """
    device = get_device() 
    model = whisper.load_model(Config.WHISPER_MODEL, device=device)
    result = model.transcribe(audio_file_path)
    return {
        "language": result["language"],
        "text": result["text"],
        "segments": result["segments"]
    }
