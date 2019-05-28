#!/usr/bin/env bash

docker-compose up --build -d

docker-compose exec web python manage.py migrate