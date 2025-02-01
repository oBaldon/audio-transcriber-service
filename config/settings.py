from dotenv import load_dotenv
import os

# Carregar o arquivo .env
load_dotenv()

class Config:
    """
    Configurações gerais do microserviço, carregadas a partir do .env.
    """
    APP_PORT = int(os.getenv("APP_PORT", 8000))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    WHISPER_MODEL = os.getenv("WHISPER_MODEL", "large")
    MAX_AUDIO_DURATION = int(os.getenv("MAX_AUDIO_DURATION", 300))
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads/")

# Instância das configurações
global_config = Config()