import whisper

def transcribe_audio(audio_file):
    # Carregar modelo Whisper
    model = whisper.load_model("large")
    
    # Salvar o arquivo temporariamente para processamento
    temp_path = "/tmp/audio_file.wav"
    audio_file.save(temp_path)
    
    # Transcrever áudio
    result = model.transcribe(temp_path)
    return result["text"]
