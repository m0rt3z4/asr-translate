# transcription_module.py

import wave
import sys
import json
from translate import translate_english_to_persian

from vosk import Model, KaldiRecognizer, SetLogLevel

def transcribe_and_translate(audio_input):
    # You can set log level to -1 to disable debug messages
    SetLogLevel(0)

    # opening the WAV file
    wf = wave.open(audio_input, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        sys.exit(1)

    # initiating the model, manually put in models folder
    # download from https://alphacephei.com/vosk/models
    model = Model("models/vosk-model-en-us-0.22-lgraph")

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    rec.SetPartialWords(True)

    # Process the WAV file
    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))

    # Gather final results
    final_result = json.loads(rec.FinalResult())
    results.append(final_result)

    # Extract text from results
    transcription_list = [res.get('text', '') for res in results if res.get('text', '')]
    transcription = " ".join(transcription_list)
    translation = translate_english_to_persian(transcription)
    return transcription, translation
