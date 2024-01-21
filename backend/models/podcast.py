from pydantic import BaseModel, field_validator
from typing import List, Optional


class PodcastCreateRequest(BaseModel):
    mindmap: List[dict]
    podcast_name: Optional[str] = "Techy Talks"
    podcast_language: Optional[str] = "en"
    presenter_name: Optional[str] = "sarah"

    @field_validator("podcast_language")
    def check_language(cls, v):
        if v not in ["en", "fr", "tr", "it", "de","es","pt"]:
            raise ValueError("Language must be either en, tr or fr")
        return v

