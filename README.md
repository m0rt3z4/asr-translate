# Automatic Speech Recognition + Tranlsate + FastAPI

## Prerequisites

- Python 3.8+
- pip
- Docker (optional, for containerized deployment)


## Environment Setup
.env
```
VOSK_MODEL_PATH = 'models/vosk-model-en-us-0.22-lgraph'
ARGOS_MODEL_PATH = 'models/translate-en_fa-1_5.argosmodel'
```
## Model Downloads

### 1. Vosk Model
- Visit the Vosk model download page: [Vosk Models](https://alphacephei.com/vosk/models)
- Download the model suitable for English, recommended: `vosk-model-en-us-0.22-lgraph`.
- Unzip the model and place it in a directory that will be referenced as `VOSK_MODEL_PATH` in your environment settings.

### 2. ArgosTranslate Model
- The ArgosTranslate models can be found at: [Argos Models](https://www.argosopentech.com/argospm/index/)
- Download the English to Persian package.
- Place the downloaded package in a location that will be referenced as `ARGOS_MODEL_PATH` in your environment settings.
- use argos_install_model.py script to install the manually downloaded model.

## Setup

```
pip install -r requirements.txt
```
to run locally:
```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
