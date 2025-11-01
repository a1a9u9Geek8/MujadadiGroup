from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create admin user if it does not exist'

    def handle(self, *args, **options):
        if not User.objects.filter(username='Mujadadi').exists():
            User.objects.create_superuser('Mujadadi', 'mujadadigroup@gmail.com', 'MujadadiGroup2024!')
            self.stdout.write(self.style.SUCCESS('Admin user created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists'))