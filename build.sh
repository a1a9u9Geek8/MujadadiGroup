#!/bin/bash
# Build script for Cloudflare Pages

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='Mujadadi').exists() or User.objects.create_superuser('Mujadadi', 'info@mujadadi.com', 'MujadadiGroup2024!')" | python manage.py shell