from django.http import HttpResponse
from django.conf import settings
import os

def debug_media(request):
    from core.models import HeroImage
    
    # Get all hero images to test URL generation
    hero_images = HeroImage.objects.all()[:5]
    
    debug_info = f"""
    <h1>Media Configuration Debug</h1>
    <p><strong>MEDIA_URL:</strong> {settings.MEDIA_URL}</p>
    <p><strong>DEFAULT_FILE_STORAGE:</strong> {getattr(settings, 'DEFAULT_FILE_STORAGE', 'Not Set')}</p>
    <h3>Hero Images in Database:</h3>
    """
    
    for image in hero_images:
        debug_info += f"""
        <div style="border: 1px solid #ccc; padding: 10px; margin: 10px 0;">
            <p><strong>Title:</strong> {image.title}</p>
            <p><strong>Image Path:</strong> {image.image}</p>
            <p><strong>Generated URL:</strong> <a href="{image.image.url}" target="_blank">{image.image.url}</a></p>
            <p><strong>Expected GitHub URL:</strong> <a href="https://raw.githubusercontent.com/a1a9u9Geek8/MujadadiGroup/main/media/{image.image}" target="_blank">https://raw.githubusercontent.com/a1a9u9Geek8/MujadadiGroup/main/media/{image.image}</a></p>
        </div>
        """
    
    return HttpResponse(debug_info)