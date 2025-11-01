from django.core.management.base import BaseCommand
from core.models import HeroImage

class Command(BaseCommand):
    help = 'Create database records for existing R2 images'

    def handle(self, *args, **options):
        # List of images that exist in R2
        r2_images = [
            'hero/farm_work.jpeg',
            'hero/chickens.jpeg',
            'hero/broilers.jpeg',
            'hero/AgricMachinery.jpeg',
        ]
        
        for image_path in r2_images:
            hero_image, created = HeroImage.objects.get_or_create(
                image=image_path,
                defaults={
                    'title': f'Hero Image - {image_path.split("/")[-1]}',
                    'is_active': True
                }
            )
            if created:
                self.stdout.write(f'Created: {hero_image.title}')
            else:
                self.stdout.write(f'Exists: {hero_image.title}')