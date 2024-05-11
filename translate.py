# translate.py

from argostranslate import package, translate

from_code = "en"
to_code = "fa"

# translatedText = translate.translate("that horse is young.", from_code, to_code)
# print(translatedText)

def translate_english_to_persian(text):
    translatedText = translate.translate(text, "en", "fa")
    return translatedText

