import random
import requests

from uuid import uuid4
from core.settings import settings


def text2speech(text, presenter_name="sarah"):
    presenters = {
        "sarah": "EXAVITQu4vr4xnSDxMaL",
        "ryan":"Yko7PKHZNXotIFUBG7I9",
    }
    if presenter_name not in presenters:
        raise ValueError(f"Unknown presenter name: {presenter_name}")

    ELEVENLABS_API_KEY = random.choice(settings.ELEVENLABS_API_KEYS.split(","))

    podcast_id = str(uuid4())

    CHUNK_SIZE = 1024
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{presenters[presenter_name]}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)
    with open(f'tmp/output_{podcast_id}.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    return podcast_id
