import whisper
from config.settings import Config

def transcribe_audio(audio_file_path: str) -> str:
    """
    Transcreve o áudio fornecido usando o modelo Whisper.

    Parâmetros:
    - audio_file_path (str): Caminho do arquivo de áudio.

    Retorna:
    - str: Transcrição do áudio.
    """
    # Exibir o modelo que será carregado
    # print(f"Carregando o modelo Whisper: {Config.WHISPER_MODEL}")

    # Carregar o modelo Whisper a partir da configuração
    model = whisper.load_model(Config.WHISPER_MODEL)

    # Transcrever o áudio
    result = model.transcribe(audio_file_path)

    # Retornar o texto transcrito
    return result.get("text", "")
