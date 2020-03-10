FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt install default-libmysqlclient-dev -y
RUN mkdir -p /app \
    && mkdir -p /app/storage/static \
    && mkdir -p /app/storage/media \
    && mkdir -p /app/logs

WORKDIR /app

ADD requirements.txt /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

#ENTRYPOINT ["/app/entrypoint.sh"]
#CMD ["prod"]
