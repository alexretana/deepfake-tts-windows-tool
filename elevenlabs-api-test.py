import requests



CHUNK_SIZE = 1024
voice_dict = {
        "Suzanne": "XFjHjl5kNbJwgzMGAfSQ",
        "Cecila": "RwoPbfqb5U2RV1wcBZLA",
        "Sofy": "6saJYDDk9wt4cuUI0FMs"
        }

base_url = "https://api.elevenlabs.io/v1/text-to-speech/"

url = base_url + voice_dict["Suzanne"]

headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "35ab3594c7ccd44ebae6ac6b3434bedf",
        }
data = {
        "text": "Alex... Do you really think it's an acomplishment to utilize eleven labs' api call via python's request pack? You're such a baka!",
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "similarity_boost": 0.75,
            "stability": 0.5,
            "style": 0.0,
            "use_speaker_boost": True
            }
        }

response = requests.request("POST", url, json=data, headers=headers)

print(response.text)

with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
        
