FROM python:3.9-slim-buster

COPY requirements.txt /
RUN apt-get -y update && \
	apt-get -y install \
	gcc \
    git \
    build-essential \
	default-libmysqlclient-dev \
	python3-dev \
    libjpeg-dev \
    zlib1g-dev \
    ffmpeg \
    libsm6 \
    libxext6

ENV PYTHONUNBUFFERED = 1

RUN python3 -m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

RUN python3 -m pip install -r requirements.txt

WORKDIR /app
