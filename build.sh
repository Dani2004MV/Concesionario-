#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python ./concesionario/manage.py collectstatic --no-input

python ./concesionario/manage.py migrate