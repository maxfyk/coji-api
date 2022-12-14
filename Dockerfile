FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED = 1
COPY requirements.txt /
COPY start.sh /start.sh
COPY firebase_key.json /firebase_key.json
COPY nginx.conf /etc/nginx/conf.d/virtual.conf

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
    libxext6 \
    nginx \
    ca-certificates \
    openssl


RUN python3 -m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
RUN python3 -m pip install -r requirements.txt



WORKDIR /app

EXPOSE 80
ENTRYPOINT ["sh", "/start.sh"]
