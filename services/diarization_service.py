import whisperx
import torch
from config.settings import Config

def assign_speakers_to_segments(segments: list, diarization_segments: list) -> list:
    """
    Associa os locutores aos segmentos conforme os tempos.
    """
    for segment in segments:
        segment["speaker"] = "unknown"
        for diar_seg in diarization_segments:
            if diar_seg["start"] <= segment["end"] and segment["start"] <= diar_seg["end"]:
                segment["speaker"] = diar_seg["speaker"]
                break
    return segments

def apply_diarization(segments: list, audio_file_path: str) -> list:
    """
    Aplica diarização e retorna os segmentos com speaker atribuído.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    diarize_model = whisperx.DiarizationPipeline(use_auth_token=Config.HUGGINGFACE_TOKEN, device=device)
    diarize_df = diarize_model(audio_file_path)
    diarize_segments = diarize_df.to_dict("records")
    return assign_speakers_to_segments(segments, diarize_segments)
