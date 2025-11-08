#!/bin/bash
# Build script for Cloudflare Pages

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Create admin user
python simple_fix.py