from django.http import HttpResponse
from core.models import HeroImage

def sync_images(request):
    if request.method == 'POST' and request.POST.get('secret') == 'sync_images_now':
        # Images that exist in GitHub
        github_images = [
            ('hero/farm_work.jpeg', 'Farm Work'),
            ('hero/chickens.jpeg', 'Chickens'),
            ('hero/broilers.jpeg', 'Broilers'),
            ('hero/AgricMachinery.jpeg', 'Agricultural Machinery'),
        ]
        
        created_count = 0
        for image_path, title in github_images:
            hero_image, created = HeroImage.objects.get_or_create(
                image=image_path,
                defaults={
                    'title': title,
                    'is_active': True,
                    'order': created_count
                }
            )
            if created:
                created_count += 1
        
        return HttpResponse(f'Synced {created_count} new images. Total images: {HeroImage.objects.count()}<br><a href="/debug-media/">Check Debug</a>')
    
    return HttpResponse('''
        <form method="post">
            <input type="hidden" name="secret" value="sync_images_now">
            <button type="submit">Sync GitHub Images to Database</button>
        </form>
    ''')