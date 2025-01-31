from fastapi.testclient import TestClient
from app import app
import os

client = TestClient(app)

def test_transcribe_endpoint():
    # Simula o upload de um arquivo de áudio válido
    with open("tests/sample_audio.wav", "rb") as audio_file:
        response = client.post("/transcribe/", files={"file": audio_file})
    
    assert response.status_code == 200
    assert "transcription" in response.json()

def test_transcribe_invalid_file():
    # Testa o upload de um arquivo inválido
    with open("tests/sample_invalid.txt", "rb") as invalid_file:
        response = client.post("/transcribe/", files={"file": invalid_file})
    
    assert response.status_code == 400
    assert "O arquivo enviado não é um áudio válido" in response.json()["detail"]
