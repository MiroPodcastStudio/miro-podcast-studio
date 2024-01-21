FROM python:3.9-slim
WORKDIR /code
RUN apt update -y && apt install -y ffmpeg
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./ /code/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]