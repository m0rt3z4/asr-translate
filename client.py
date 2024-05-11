# client.py

import requests

def upload_audio_and_get_translation(url, file_path):
    # Open the WAV file in binary mode
    with open(file_path, 'rb') as f:
        files = {'file': (file_path, f, 'audio/wav')}
        
        # Send the POST request with the file
        response = requests.post(url, files=files)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Translation successful!")
            print("Response:", response.json())
        else:
            print(f"Failed to translate. Status code: {response.status_code}")
            print("Response:", response.json())

# URL of the FastAPI endpoint
api_url = 'http://127.0.0.1:8000/translate/'

# Path to the audio file you want to upload
audio_file_path = 'samples/sample3.wav'

# Call the function to upload the file and get translation
upload_audio_and_get_translation(api_url, audio_file_path)