from django.http import HttpResponse
from core.models import HeroImage

def sync_images(request):
    if request.method == 'POST' and request.POST.get('secret') == 'sync_images_now':
        # Images that exist in GitHub
        github_images = [
            'hero/farm_work.jpeg',
            'hero/chickens.jpeg',
            'hero/broilers.jpeg',
            'hero/AgricMachinery.jpeg',
        ]
        
        created_count = 0
        for image_path in github_images:
            hero_image, created = HeroImage.objects.get_or_create(
                image=image_path,
                defaults={
                    'title': f'Hero Image - {image_path.split("/")[-1]}',
                    'is_active': True
                }
            )
            if created:
                created_count += 1
        
        return HttpResponse(f'Synced {created_count} new images. Total images: {HeroImage.objects.count()}')
    
    return HttpResponse('''
        <form method="post">
            <input type="hidden" name="secret" value="sync_images_now">
            <button type="submit">Sync GitHub Images to Database</button>
        </form>
    ''')