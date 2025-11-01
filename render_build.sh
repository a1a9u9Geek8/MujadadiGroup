#!/usr/bin/env bash
# Render build script

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py setup_admin

# Also create via direct command as backup
echo "from django.contrib.auth.models import User; u, created = User.objects.get_or_create(username='Mujadadi', defaults={'email': 'mujadadigroup@gmail.com', 'is_superuser': True, 'is_staff': True}); u.set_password('MujadadiGroup2024!') if created else None; u.save()" | python manage.py shell