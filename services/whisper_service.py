import whisper

def transcribe_audio(audio_file_path: str) -> str:
    """
    Transcreve o áudio fornecido usando o modelo Whisper.

    Parâmetros:
    - audio_file_path (str): Caminho do arquivo de áudio.

    Retorna:
    - str: Transcrição do áudio.
    """
    # Carregar o modelo Whisper
    model = whisper.load_model("large")

    # Transcrever o áudio
    result = model.transcribe(audio_file_path)

    # Retornar o texto transcrito
    return result.get("text", "")
