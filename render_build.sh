#!/usr/bin/env bash
# Render build script

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py setup_admin