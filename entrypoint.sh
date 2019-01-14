#!/bin/bash

set -e

cd /src

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

coverage run manage.py test -v 2
coverage report

python3 manage.py runserver 0.0.0.0:8000
