#!/bin/bash

GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
GIT_SHA=$(git rev-parse --short HEAD)
TAG=${GIT_BRANCH}-${GIT_SHA}-$(date +%s)

# Log into GCP artifact registry
gcloud auth print-access-token |
	docker login -u oauth2accesstoken --password-stdin https://us-east1-docker.pkg.dev

docker build -t us-east1-docker.pkg.dev/everythingisacomputer/everythingisacomputer/api-cardealassist:$TAG . --target prod
docker push us-east1-docker.pkg.dev/everythingisacomputer/everythingisacomputer/api-cardealassist:$TAG
