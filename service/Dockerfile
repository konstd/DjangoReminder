FROM python:3.8.2-buster
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app \
    && mkdir -p /app/service/static \
    && mkdir -p /app/service/media \
    && mkdir -p /app/service/logs \
    && mkdir -p /app/service/reports

WORKDIR /app

ADD requirements.txt /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /app
