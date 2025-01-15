from flask import Blueprint, request, jsonify
from app.services.transcriber import transcribe_audio

transcribe_bp = Blueprint("transcribe", __name__)

@transcribe_bp.route("/", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "Audio file is required"}), 400

    audio_file = request.files["audio"]
    try:
        transcription = transcribe_audio(audio_file)
        return jsonify({"transcription": transcription}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
