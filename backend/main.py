import traceback
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models.podcast import PodcastCreateRequest
from controllers.podcast_controller import podcast_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/podcast")
async def create_podcast(request: PodcastCreateRequest):
    try:
        return podcast_controller.create_podcast(request.mindmap, request.podcast_name, request.presenter_name, request.podcast_language)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=500, detail="Unexpected error while creating podcast.")
