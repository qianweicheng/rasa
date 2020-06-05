#!/usr/bin/env bash
set -e
ROOT_DIR=$(cd "$(dirname "$0")/..";pwd)
cd $ROOT_DIR

docker build -t hub.edisonpark.net/edisonchat/rasa:tools -f ./docker/Dockerfile_full .
docker push hub.edisonpark.net/edisonchat/rasa:tools


# docker build -t rasa_test -f ./deploy/Dockerfile . ;\
# docker run -it --rm --entrypoint bash rasa_test
# docker run --rm rasa_test
# python -m edo_pro.rasasc_jeff -r
# run via docker 
# docker run -it --rm \
# --name rasa \
# -v `pwd`/edo_pro:/app/edo_pro \
# -p 5006:5005 \
# --entrypoint python \
# hub.edisonpark.net/edisonchat/rasa:tools \
# -m edo_pro.rasasc_jeff -r