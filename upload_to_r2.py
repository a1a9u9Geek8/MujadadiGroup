#!/usr/bin/env python3
import os
import boto3
from pathlib import Path

# R2 Configuration
ACCESS_KEY = 'your-actual-access-key-id'
SECRET_KEY = 'your-actual-secret-access-key'
ENDPOINT_URL = 'https://your-account-id.r2.cloudflarestorage.com'
BUCKET_NAME = 'mujadadi-media'

# Initialize R2 client
s3_client = boto3.client(
    's3',
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name='auto'
)

def upload_media_files():
    media_dir = Path('media')
    
    for file_path in media_dir.rglob('*'):
        if file_path.is_file():
            # Get relative path from media directory
            relative_path = file_path.relative_to(media_dir)
            
            # Upload to R2
            try:
                s3_client.upload_file(
                    str(file_path),
                    BUCKET_NAME,
                    str(relative_path),
                    ExtraArgs={'ACL': 'public-read'}
                )
                print(f"Uploaded: {relative_path}")
            except Exception as e:
                print(f"Error uploading {relative_path}: {e}")

if __name__ == '__main__':
    upload_media_files()
    print("Upload complete!")