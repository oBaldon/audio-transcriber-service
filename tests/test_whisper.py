import pytest
from services.whisper_service import transcribe_audio

def test_transcribe_audio_valid():
    # Teste com áudio válido
    transcription = transcribe_audio("tests/sample_audio.wav")
    assert isinstance(transcription, str), "A transcrição não retornou uma string."
    assert len(transcription) > 0, "A transcrição está vazia."

def test_transcribe_audio_invalid_path():
    # Testa se um caminho inválido lança uma RuntimeError, já que o whisper depende do ffmpeg
    with pytest.raises(RuntimeError, match="Failed to load audio"):
        transcribe_audio("invalid_path.wav")
