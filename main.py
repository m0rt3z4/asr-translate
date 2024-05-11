# main.py

from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import shutil
import os

from translate import translate_english_to_persian
from transcription_module import transcribe_and_translate  # Import your transcription function

app = FastAPI()

class TranslationResult(BaseModel):
    transcription: str
    translation: str

@app.post("/translate/", response_model=TranslationResult)
async def translate_audio(file: UploadFile = File(...)):
    if file.content_type != 'audio/wav':
        raise HTTPException(status_code=400, detail="Only WAV files are supported.")

    try:
        # Save temporary audio file
        temp_file_path = f"temp/temp_{file.filename}"
        with open(temp_file_path, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Transcribe and translate the audio file
        transcription, translation = transcribe_and_translate(temp_file_path)

        # Clean up the temporary file
        os.remove(temp_file_path)

        return TranslationResult(transcription=transcription, translation=translation)

    except Exception as e:
        # Clean up in case of failure
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        raise HTTPException(status_code=500, detail=str(e))