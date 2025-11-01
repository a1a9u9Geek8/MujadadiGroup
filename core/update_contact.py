from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from core.models import ContactInfo

@csrf_exempt
def update_contact(request):
    if request.method == 'POST' and request.POST.get('secret') == 'update_contact_now':
        contact, created = ContactInfo.objects.get_or_create(
            is_active=True,
            defaults={
                'head_office': 'No. 14, Ganbe Village, Oke Oyi, Opposite Ilorin East Local Government Secretariat, Ilorin, Kwara State, Nigeria.',
                'annex_office': 'No. 1, Opposite Ilorin West Shopping Complex, Ilorin, Kwara State.',
                'phone_numbers': '+234 703 199 6548|+1 (240) 264-0244|+234 706 360 9416',
                'email': 'info@mujadadi.com'
            }
        )
        
        if not created:
            contact.head_office = 'No. 14, Ganbe Village, Oke Oyi, Opposite Ilorin East Local Government Secretariat, Ilorin, Kwara State, Nigeria.'
            contact.annex_office = 'No. 1, Opposite Ilorin West Shopping Complex, Ilorin, Kwara State.'
            contact.save()
        
        return HttpResponse(f'Contact info {"created" if created else "updated"} successfully!')
    
    return HttpResponse('''
        <form method="post">
            <input type="hidden" name="secret" value="update_contact_now">
            <button type="submit">Update Contact Information</button>
        </form>
    ''')