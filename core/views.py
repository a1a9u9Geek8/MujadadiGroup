from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import Category, HeroImage, Gallery, ContactMessage, ContactInfo, TeamMember, JobApplication, InvestorRelation, Sustainability, NewsMedia
from .forms import ContactForm, JobApplicationForm

def home(request):
    categories = Category.objects.all()
    hero_images = HeroImage.objects.filter(is_active=True)[:3]
    featured_gallery = Gallery.objects.filter(is_featured=True)[:8]
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    investor_relations = InvestorRelation.objects.filter(featured=True)[:3]
    sustainability = Sustainability.objects.filter(featured=True)[:3]
    news_media = NewsMedia.objects.filter(featured=True)[:3]
    return render(request, "core/index.html", {
        "categories": categories, 
        "hero_images": hero_images,
        "featured_gallery": featured_gallery,
        "contact_info": contact_info,
        "investor_relations": investor_relations,
        "sustainability": sustainability,
        "news_media": news_media
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    return render(request, "core/category_detail.html", {"category": category, "contact_info": contact_info})

def about(request):
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    team_members = TeamMember.objects.filter(is_active=True)
    return render(request, "core/about.html", {"contact_info": contact_info, "team_members": team_members})

def careers(request):
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            
            # Send email notification to company
            try:
                subject = f"New Job Application: {application.get_position_applied_display()}"
                html_content = render_to_string('core/email/job_application_notification.html', {
                    'application': application
                })
                
                email = EmailMultiAlternatives(
                    subject,
                    f"New job application from {application.first_name} {application.last_name}",
                    settings.DEFAULT_FROM_EMAIL,
                    [contact_info.email if contact_info else 'mujadadigroup@gmail.com'],
                )
                email.attach_alternative(html_content, "text/html")
                email.attach_file(application.cv_file.path)
                email.send()
            except Exception as e:
                print(f"Job application email failed: {e}")
            
            # Send confirmation email to applicant
            try:
                confirmation_subject = "Application Received - Mujadadi Group"
                confirmation_html = render_to_string('core/email/job_application_confirmation.html', {
                    'application': application
                })
                
                confirmation_email = EmailMultiAlternatives(
                    confirmation_subject,
                    f"Thank you for your application, {application.first_name}!",
                    settings.DEFAULT_FROM_EMAIL,
                    [application.email],
                )
                confirmation_email.attach_alternative(confirmation_html, "text/html")
                confirmation_email.send()
            except Exception as e:
                print(f"Job confirmation email failed: {e}")
            
            messages.success(request, 'Thank you for your application! We will review it and get back to you soon.')
            return redirect('careers')
    else:
        form = JobApplicationForm()
    return render(request, "core/careers.html", {"contact_info": contact_info, "form": form})

def contact(request):
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            # Send email notification to company
            try:
                subject = f"New Contact Message: {contact_message.subject}"
                html_content = render_to_string('core/email/contact_notification.html', {
                    'contact_message': contact_message
                })
                
                email = EmailMultiAlternatives(
                    subject,
                    f"New contact message from {contact_message.first_name} {contact_message.last_name}",
                    settings.DEFAULT_FROM_EMAIL,
                    [contact_info.email if contact_info else 'mujadadigroup@gmail.com'],
                )
                email.attach_alternative(html_content, "text/html")
                email.send()
            except Exception as e:
                print(f"Company email sending failed: {e}")
            
            # Send confirmation email to user
            try:
                confirmation_subject = "Thank you for contacting Mujadadi Group"
                confirmation_html = render_to_string('core/email/contact_confirmation.html', {
                    'contact_message': contact_message
                })
                
                confirmation_email = EmailMultiAlternatives(
                    confirmation_subject,
                    f"Thank you for your message, {contact_message.first_name}!",
                    settings.DEFAULT_FROM_EMAIL,
                    [contact_message.email],
                )
                confirmation_email.attach_alternative(confirmation_html, "text/html")
                confirmation_email.send()
            except Exception as e:
                print(f"Confirmation email sending failed: {e}")
            
            messages.success(request, 'Thank you for your message! We will get back to you within 24 hours.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"contact_info": contact_info, "form": form})

def agriculture_detail(request):
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    return render(request, "core/agriculture_detail.html", {"contact_info": contact_info})

def privacy_policy(request):
    return render(request, "core/privacy_policy.html")

def terms_of_service(request):
    return render(request, "core/terms_of_service.html")

def investor_relations(request):
    items = InvestorRelation.objects.all().order_by('-created_at')
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    return render(request, "core/investor_relations.html", {
        "items": items,
        "contact_info": contact_info
    })

def sustainability(request):
    items = Sustainability.objects.all().order_by('-created_at')
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    return render(request, "core/sustainability.html", {
        "items": items,
        "contact_info": contact_info
    })

def news_media(request):
    items = NewsMedia.objects.all().order_by('-created_at')
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    return render(request, "core/news_media.html", {
        "items": items,
        "contact_info": contact_info
    })
