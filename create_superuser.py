#!/usr/bin/env python
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mujsettings.settings')
django.setup()

from django.contrib.auth.models import User

username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'mujadadigroup@gmail.com')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'MujadadiAdmin2024!')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superuser {username} created successfully')
else:
    print(f'Superuser {username} already exists')