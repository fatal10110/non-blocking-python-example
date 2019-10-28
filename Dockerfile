FROM python:3.7-alpine

RUN pip install requests && pip install flask && pip install aiohttp

ENV PYTHONPATH /example
WORKDIR /example