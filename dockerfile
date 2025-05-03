FROM alpine:3.21.3

RUN apk update --no-cache && \
    apk upgrade --no-cache 

RUN apk add \
    python3 \
    pipx

RUN pipx install requests --include-deps --global 

RUN mkdir -p /scripts
COPY ./scripts /scripts

VOLUME [ "/configuration" ]

CMD ["python3","/scripts/init.py"]

LABEL org.opencontainers.image.source=https://github.com/martinspaniol/firefly-iii-init
LABEL org.opencontainers.image.description="firefly-iii-init"
LABEL org.opencontainers.image.licenses=MIT