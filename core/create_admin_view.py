from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_admin(request):
    if request.method == 'POST' and request.POST.get('secret') == 'create_admin_now':
        if not User.objects.filter(username='Mujadadi').exists():
            User.objects.create_superuser('Mujadadi', 'mujadadigroup@gmail.com', 'MujadadiGroup2024!')
            return HttpResponse('Admin user created successfully')
        else:
            return HttpResponse('Admin user already exists')
    return HttpResponse('Invalid request')