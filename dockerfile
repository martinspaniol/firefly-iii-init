FROM ghcr.io/linuxserver/baseimage-alpine:3.16


RUN apk update --no-cache && \
    apk upgrade --no-cache 

RUN apk add \
    python3 \
    py3-pip

RUN python3 -m pip install --upgrade pip
RUN pip3 install requests

VOLUME [ "/scripts" ]