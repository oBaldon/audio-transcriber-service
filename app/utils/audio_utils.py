from pydub import AudioSegment

def convert_to_wav(audio_file, output_path):
    """Converte arquivos de áudio para WAV. (Whisper ja faz isso)"""
    audio = AudioSegment.from_file(audio_file)
    audio.export(output_path, format="wav")
    return output_path
