from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def create_admin(request):
    message = None
    if request.method == 'POST' and request.POST.get('secret') == 'create_admin_now':
        if not User.objects.filter(username='Mujadadi').exists():
            User.objects.create_superuser('Mujadadi', 'mujadadigroup@gmail.com', 'MujadadiGroup2024!')
            message = 'Admin user created successfully! Username: Mujadadi, Password: MujadadiGroup2024!'
        else:
            message = 'Admin user already exists'
    return render(request, 'core/create_admin.html', {'message': message})