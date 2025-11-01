#!/usr/bin/env python3
import requests

# Test URLs
urls = [
    "https://media.mujadadigroup.com/hero/farm_work.jpeg",
    "https://21b2ba3dc9c06196638ff51b74be82f5.r2.cloudflarestorage.com/mujadadi-media/hero/farm_work.jpeg",
    "https://mujadadi-media.21b2ba3dc9c06196638ff51b74be82f5.r2.cloudflarestorage.com/hero/farm_work.jpeg"
]

for url in urls:
    try:
        response = requests.head(url, timeout=10)
        print(f"✅ {url} - Status: {response.status_code}")
    except Exception as e:
        print(f"❌ {url} - Error: {e}")