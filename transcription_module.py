import wave
import sys
import json
from translate import translate_english_to_persian
from vosk import Model, KaldiRecognizer, SetLogLevel
import os
from dotenv import load_dotenv

load_dotenv()

def transcribe_and_translate(audio_input):
    SetLogLevel(0)

    wf = wave.open(audio_input, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        raise ValueError("Audio file must be WAV format mono PCM.")

    model_path = os.getenv('VOSK_MODEL_PATH')
    model = Model(model_path)

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    rec.SetPartialWords(True)

    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))

    final_result = json.loads(rec.FinalResult())
    results.append(final_result)

    transcription_list = [res.get('text', '') for res in results if res.get('text', '')]
    transcription = " ".join(transcription_list)
    translation = translate_english_to_persian(transcription)
    return transcription, translation