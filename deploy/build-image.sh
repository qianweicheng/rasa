#!/usr/bin/env bash
set -e
ROOT_DIR=$(cd "$(dirname "$0")/..";pwd)
cd $ROOT_DIR

docker build -t hub.edisonpark.net/edisonchat/rasa:tools -f ./deploy/Dockerfile .
docker push hub.edisonpark.net/edisonchat/rasa:tools