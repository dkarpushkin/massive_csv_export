FROM python:3.7.3-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev build-essential

RUN mkdir -p /opt/project
WORKDIR /opt/project

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

ADD . ./