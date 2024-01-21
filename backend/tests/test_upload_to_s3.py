import boto3
from botocore.client import Config
podcast_id = "podcast_d4d760bf-c5f4-4ab1-ae1a-4cbcddef85c6.mp3"
s3 = boto3.resource('s3', region_name="eu-west-2",
                    config=Config(signature_version='s3v4'))
bucket = s3.Bucket('miro-to-podcast')
bucket.put_object(
    Key=f"podcast_{podcast_id}.mp3", Body=open(f"tmp/podcast_{podcast_id}.mp3", 'rb'), ACL='public-read')
