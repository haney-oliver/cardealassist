#!/bin/bash

GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
GIT_SHA=$(git rev-parse --short HEAD)
TAG=${GIT_BRANCH}-${GIT_SHA}-$(date +%s)

docker build -t registry.dev.everythingisacomputer.io/api-cardealassist:$TAG . --target prod
docker push registry.dev.everythingisacomputer.io/api-cardealassist:$TAG
