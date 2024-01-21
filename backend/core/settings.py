import os
from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ELEVENLABS_API_KEYS: str = os.getenv("ELEVENLABS_API_KEYS", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")


settings = Settings()