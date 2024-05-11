from argostranslate import package, translate
# import os
from dotenv import load_dotenv

load_dotenv()

def translate_english_to_persian(text):
    # Check model instalization
    # if not package.is_installed(from_code="en", to_code="fa"):
    #     model_path = os.getenv('ARGOS_MODEL_PATH')
    #     package.install_from_path(model_path)
    translatedText = translate.translate(text, "en", "fa")
    return translatedText

