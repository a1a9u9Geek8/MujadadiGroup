from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def create_admin(request):
    message = None
    if request.method == 'POST' and request.POST.get('secret') == 'create_admin_now':
        # Always ensure admin exists with correct password
        user, created = User.objects.get_or_create(
            username='Mujadadi',
            defaults={
                'email': 'mujadadigroup@gmail.com',
                'is_superuser': True,
                'is_staff': True
            }
        )
        user.set_password('MujadadiGroup2024!')
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        if created:
            message = 'Admin user created successfully! Username: Mujadadi, Password: MujadadiGroup2024!'
        else:
            message = 'Admin user updated successfully! Username: Mujadadi, Password: MujadadiGroup2024!'
    return render(request, 'core/create_admin.html', {'message': message})