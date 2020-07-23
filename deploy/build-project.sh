#!/usr/bin/env bash
set -e
ROOT_DIR=$(cd "$(dirname "$0")/..";pwd)
cd $ROOT_DIR
if [[ ! -d "venv" ]];then
    virtualenv -p python3 venv
    pip install -r requirements.txt
    pip install -e .
fi
. venv/bin/activate
python -m edo_pro.wangxy.XY_rasa_04 -r
deactivate
