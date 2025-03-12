#!/bin/bash

docker-compose build
docker-compose up -d
sleep 10
docker-compose exec web python app/database.py

