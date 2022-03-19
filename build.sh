#!/bin/bash

docker build -t humanseg -f Dockerfile.cpu . --force-rm
docker-compose up -d