#!/usr/bin/env python
"""
Simple script to create admin user - run this once after deployment
"""
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mujsettings.settings')
django.setup()

from django.contrib.auth.models import User

# Create admin user
username = 'admin'
email = 'mujadadigroup@gmail.com'
password = 'admin123'

# Delete existing admin users
User.objects.filter(username__in=['admin', 'Mujadadi']).delete()

# Create new superuser
user = User.objects.create_superuser(username=username, email=email, password=password)
print(f'Admin user created: {username} / {password}')