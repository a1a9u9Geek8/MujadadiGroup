from django.http import HttpResponse
from django.contrib.auth.models import User

def create_admin(request):
    # Delete existing users
    User.objects.filter(username__in=['admin', 'Mujadadi']).delete()
    
    # Create admin user
    user = User.objects.create_superuser(
        username='admin',
        email='mujadadigroup@gmail.com', 
        password='admin123'
    )
    
    return HttpResponse('Admin created: username=admin, password=admin123')