import torch
from config.settings import Config

def get_device():
    """
    Retorna o tipo de dispositivo a ser usado ('cuda' ou 'cpu'),
    baseado no .env ou na disponibilidade automática.
    """
    device_type = Config.DEVICE_TYPE.lower()
    if device_type == "cuda":
        return "cuda"
    elif device_type == "cpu":
        return "cpu"
    else:  # auto
        return "cuda" if torch.cuda.is_available() else "cpu"
