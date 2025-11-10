from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User

def debug_database(request):
    db_info = settings.DATABASES['default']
    user_count = User.objects.count()
    
    response = f"""
    Database Engine: {db_info.get('ENGINE', 'Unknown')}
    Database Name: {db_info.get('NAME', 'Unknown')}
    User Count: {user_count}
    
    Users in database:
    """
    
    for user in User.objects.all():
        response += f"- {user.username} (superuser: {user.is_superuser})\n"
    
    return HttpResponse(response, content_type='text/plain')