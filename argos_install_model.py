from argostranslate import package, translate
import os
from dotenv import load_dotenv

load_dotenv()
model_path = os.getenv('ARGOS_MODEL_PATH')
package.install_from_path(model_path)
