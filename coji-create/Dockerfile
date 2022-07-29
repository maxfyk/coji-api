FROM python:3.10-slim-buster

COPY requirements.txt /
RUN apt-get -y update && \
	apt-get -y install \
	gcc \
	default-libmysqlclient-dev \
	python3-dev
RUN python3 -m pip install -r requirements.txt

COPY . /app
WORKDIR /app
ENV PYTHONUNBUFFERED = 1