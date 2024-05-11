from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
import aiofiles
import os

from transcription_module import transcribe_and_translate

app = FastAPI()

class TranslationResult(BaseModel):
    transcription: str
    translation: str

@app.post("/translate/", response_model=TranslationResult)
async def translate_audio(file: UploadFile = File(...)):
    if file.content_type != 'audio/wav':
        raise HTTPException(status_code=400, detail="Only WAV files are supported.")

    temp_file_path = f"{file.filename}_temp"
    try:
        async with aiofiles.open(temp_file_path, 'wb') as buffer:
            await buffer.write(await file.read())

        transcription, translation = await run_in_threadpool(
            transcribe_and_translate, temp_file_path
        )

        return TranslationResult(transcription=transcription, translation=translation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(temp_file_path):
            await run_in_threadpool(os.remove, temp_file_path)
