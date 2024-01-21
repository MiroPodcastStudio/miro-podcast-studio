import boto3
from botocore.client import Config
from pydub import AudioSegment


def merge_and_upload(podcast_id):
    intro = AudioSegment.from_mp3("intro.mp3")
    content = AudioSegment.from_mp3(f"tmp/output_{podcast_id}.mp3")
    outro = AudioSegment.from_mp3("outro.mp3")
    combined_sounds = intro + content + outro
    combined_sounds.export(f"tmp/podcast_{podcast_id}.mp3", format="mp3")
    s3 = boto3.resource('s3', region_name="eu-west-2",
                        config=Config(signature_version='s3v4'))
    bucket = s3.Bucket('miro-to-podcast')
    bucket.put_object(
        Key=f"podcast_{podcast_id}.mp3", Body=open(f"tmp/podcast_{podcast_id}.mp3", 'rb'), ACL='public-read')

    access_url = "https://miro-to-podcast.s3.eu-west-2.amazonaws.com/" + \
        f"podcast_{podcast_id}.mp3"
    
    return access_url
