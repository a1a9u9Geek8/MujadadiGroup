#!/usr/bin/env bash
# Render build script

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate

# Create superuser - multiple attempts
python manage.py setup_admin

# Force create admin user
echo "from django.contrib.auth.models import User; u, created = User.objects.get_or_create(username='Mujadadi', defaults={'email': 'mujadadigroup@gmail.com', 'is_superuser': True, 'is_staff': True}); u.set_password('MujadadiGroup2024!'); u.is_superuser = True; u.is_staff = True; u.save(); print(f'Admin user: {u.username}, Active: {u.is_active}, Staff: {u.is_staff}, Super: {u.is_superuser}')" | python manage.py shell