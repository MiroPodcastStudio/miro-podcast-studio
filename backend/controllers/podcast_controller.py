from utils.mindmap import MindMap
from utils.elevenlabs import text2speech
from utils.merger import merge_and_upload
import logging


class PodcastController:
    def __init__(self) -> None:
        pass

    def create_podcast(self, mindmap, podcast_name, presenter_name, podcast_language="en"):
        logging.info("Creating podcast")
        mindmap_instance = MindMap(mindmap)
        mindmap_csv = mindmap_instance.export_to_str()
        podcast_text = mindmap_instance.create_podcast_text(
            mindmap_csv, podcast_name, presenter_name, podcast_language)
        podcast_id = text2speech(podcast_text, presenter_name)
        title = mindmap_instance.create_podcast_title(podcast_text)
        access_url = merge_and_upload(podcast_id)
        return {"url": access_url, "title": title, "language": podcast_language, "presenter": presenter_name, "presenter_image":f"https://miro-to-podcast.s3.eu-west-2.amazonaws.com/{presenter_name}.jpg"}


podcast_controller = PodcastController()
