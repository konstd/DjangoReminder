FROM python:3.8.2-alpine3.11
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app \
    && mkdir -p /app/storage/static \
    && mkdir -p /app/storage/media \
    && mkdir -p /app/logs

WORKDIR /app

ADD requirements.txt /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /app
