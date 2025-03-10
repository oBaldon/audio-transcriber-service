import whisperx
import torch
from config.settings import Config

def align_segments(segments: list, audio_file_path: str, language: str) -> list:
    """
    Alinha os segmentos por palavra usando WhisperX.
    Retorna segmentos com alinhamento.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    audio = whisperx.load_audio(audio_file_path)
    model_a, metadata = whisperx.load_align_model(language_code=language, device=device)
    result_aligned = whisperx.align(segments, model_a, metadata, audio, device)
    return result_aligned["segments"]
