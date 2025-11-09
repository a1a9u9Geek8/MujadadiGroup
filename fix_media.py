#!/usr/bin/env python
"""
Simple fix: Change MEDIA_URL to serve from Render directly
"""
import os

# Read settings file
with open('mujsettings/settings.py', 'r') as f:
    content = f.read()

# Replace GitHub URL with Render URL for media
content = content.replace(
    "MEDIA_URL = 'https://raw.githubusercontent.com/a1a9u9Geek8/MujadadiGroup/main/media/'",
    "MEDIA_URL = '/media/'"
)

# Write back
with open('mujsettings/settings.py', 'w') as f:
    f.write(content)

print("Fixed: Images will now be served from Render")