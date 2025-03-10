import os
import json
from fastapi import UploadFile

async def save_upload_file(upload_file: UploadFile, destination_folder: str = "temp") -> str:
    os.makedirs(destination_folder, exist_ok=True)
    temp_file_path = os.path.join(destination_folder, upload_file.filename)
    try:
        with open(temp_file_path, "wb") as temp_file:
            content = await upload_file.read()
            temp_file.write(content)
    finally:
        await upload_file.close()
    return temp_file_path


def save_json_result(data: dict, original_filename: str, destination_folder: str = "temp") -> str:
    os.makedirs(destination_folder, exist_ok=True)
    json_path = os.path.join(destination_folder, f"{os.path.splitext(original_filename)[0]}.json")
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    return json_path


def save_srt_result(segments: list, original_filename: str, destination_folder: str = "temp") -> str:
    os.makedirs(destination_folder, exist_ok=True)
    srt_path = os.path.join(destination_folder, f"{os.path.splitext(original_filename)[0]}.srt")

    def format_time(seconds: float) -> str:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds - int(seconds)) * 1000)
        return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

    with open(srt_path, "w", encoding="utf-8") as srt_file:
        for idx, segment in enumerate(segments, start=1):
            start = format_time(segment["start"])
            end = format_time(segment["end"])
            text = segment["text"]
            srt_file.write(f"{idx}\n{start} --> {end}\n{text}\n\n")

    return srt_path
