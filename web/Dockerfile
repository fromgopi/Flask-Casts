FROM python:3.6.1
MAINTAINER Gopi KrishnaM

RUN addgroup flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask

RUN mkdir -p /home/flask/app/web

WORKDIR /home/flask/app/web

COPY . /home/flask/app/web
RUN pip install --no-cache-dir -r requirements.txt

RUN chown -R flask:flaskgroup /home/flask

USER flask