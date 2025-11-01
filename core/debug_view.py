from django.http import HttpResponse
from django.conf import settings
import os

def debug_media(request):
    from core.models import HeroImage
    
    # Get a sample image to test URL generation
    sample_image = HeroImage.objects.first()
    sample_url = sample_image.image.url if sample_image else 'No images found'
    
    debug_info = f"""
    <h1>Media Configuration Debug</h1>
    <p><strong>USE_R2_STORAGE:</strong> {os.getenv('USE_R2_STORAGE', 'Not Set')}</p>
    <p><strong>R2_ACCESS_KEY_ID:</strong> {os.getenv('R2_ACCESS_KEY_ID', 'Not Set')[:10]}...</p>
    <p><strong>R2_BUCKET_NAME:</strong> {os.getenv('R2_BUCKET_NAME', 'Not Set')}</p>
    <p><strong>R2_ENDPOINT_URL:</strong> {os.getenv('R2_ENDPOINT_URL', 'Not Set')}</p>
    <p><strong>R2_CUSTOM_DOMAIN:</strong> {os.getenv('R2_CUSTOM_DOMAIN', 'Not Set')}</p>
    <p><strong>MEDIA_URL:</strong> {settings.MEDIA_URL}</p>
    <p><strong>DEFAULT_FILE_STORAGE:</strong> {getattr(settings, 'DEFAULT_FILE_STORAGE', 'Not Set')}</p>
    <p><strong>Sample Image URL:</strong> <a href="{sample_url}" target="_blank">{sample_url}</a></p>
    <p><strong>Test Direct Access:</strong> <a href="https://media.mujadadigroup.com/hero/farm_work.jpeg" target="_blank">https://media.mujadadigroup.com/hero/farm_work.jpeg</a></p>
    """
    return HttpResponse(debug_info)