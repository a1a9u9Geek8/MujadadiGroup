#!/usr/bin/env python
import os
import django
from django.conf import settings

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mujsettings.settings')
django.setup()

from django.contrib.auth.models import User

# Create or update admin user
username = 'Mujadadi'
email = 'admin@mujadadi.com'
password = 'MujadadiGroup2024!'

try:
    user = User.objects.get(username=username)
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f"Updated existing admin user: {username}")
except User.DoesNotExist:
    User.objects.create_superuser(username, email, password)
    print(f"Created new admin user: {username}")