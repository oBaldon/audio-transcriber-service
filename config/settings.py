from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

class Config:
    APP_PORT = int(os.getenv("APP_PORT", 8000))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    WHISPER_MODEL = os.getenv("WHISPER_MODEL", "large")
    MAX_AUDIO_DURATION = int(os.getenv("MAX_AUDIO_DURATION", 300))
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "temp/")
    HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN", None)
    DEVICE_TYPE = os.getenv("DEVICE_TYPE", "auto")  # valores possíveis: 'cuda', 'cpu', 'auto'

global_config = Config()
