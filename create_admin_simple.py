#!/usr/bin/env python
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mujsettings.settings')
django.setup()

from django.contrib.auth.models import User

try:
    user, created = User.objects.get_or_create(
        username='Mujadadi',
        defaults={
            'email': 'admin@mujadadi.com',
            'is_staff': True,
            'is_superuser': True,
            'is_active': True,
        }
    )
    user.set_password('MujadadiGroup2024!')
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.save()
    print("Admin user created/updated successfully!")
except Exception as e:
    print(f"Error: {e}")