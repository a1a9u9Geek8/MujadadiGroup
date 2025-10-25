from django.contrib import admin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import timezone
from .models import Category, Service, Gallery, HeroImage, ContactMessage, ContactInfo, Newsletter, TeamMember, JobApplication

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['category']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'created_at']
    list_filter = ['category', 'is_featured', 'created_at']
    list_editable = ['is_featured']

@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order']
    list_editable = ['is_active', 'order']

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'updated_at']
    fieldsets = (
        ('Office Locations', {
            'fields': ('head_office', 'annex_office')
        }),
        ('Contact Details', {
            'fields': ('phone_numbers', 'email')
        }),
        ('Social Media', {
            'fields': ('instagram', 'facebook', 'twitter')
        }),
        ('Settings', {
            'fields': ('is_active',)
        }),
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['business_unit', 'is_read', 'created_at', 'newsletter']
    list_editable = ['is_read']
    readonly_fields = ['created_at']
    search_fields = ['first_name', 'last_name', 'email', 'subject', 'company']
    fieldsets = (
        ('Contact Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'company')
        }),
        ('Message Details', {
            'fields': ('business_unit', 'subject', 'message')
        }),
        ('Settings', {
            'fields': ('newsletter', 'is_read', 'created_at')
        }),
    )
    
    def has_add_permission(self, request):
        return False


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'is_sent', 'sent_at', 'recipients_count']
    list_filter = ['is_sent', 'created_at']
    readonly_fields = ['sent_at', 'recipients_count']
    actions = ['send_newsletter']
    
    def send_newsletter(self, request, queryset):
        sent_count = 0
        for newsletter in queryset.filter(is_sent=False):
            subscribers = newsletter.get_subscribers()
            if subscribers:
                html_content = render_to_string('core/email/newsletter.html', {
                    'newsletter': newsletter
                })
                
                email = EmailMultiAlternatives(
                    newsletter.subject,
                    f"Newsletter: {newsletter.title}",
                    settings.DEFAULT_FROM_EMAIL,
                    list(subscribers),
                )
                email.attach_alternative(html_content, "text/html")
                email.send()
                
                newsletter.is_sent = True
                newsletter.sent_at = timezone.now()
                newsletter.recipients_count = len(subscribers)
                newsletter.save()
                sent_count += 1
        
        self.message_user(request, f'Successfully sent {sent_count} newsletters.')
    
    send_newsletter.short_description = "Send selected newsletters"


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'category', 'is_active', 'order']
    list_filter = ['category', 'is_active', 'joined_date']
    list_editable = ['order', 'is_active']
    search_fields = ['name', 'position']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'position', 'category', 'bio', 'image')
        }),
        ('Contact Information', {
            'fields': ('email', 'linkedin')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'position_applied', 'experience_years', 'created_at', 'is_reviewed']
    list_filter = ['position_applied', 'is_reviewed', 'created_at', 'experience_years']
    list_editable = ['is_reviewed']
    readonly_fields = ['created_at']
    search_fields = ['first_name', 'last_name', 'email', 'position_applied']
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Application Details', {
            'fields': ('position_applied', 'experience_years', 'cover_letter', 'cv_file')
        }),
        ('Review', {
            'fields': ('is_reviewed', 'notes', 'created_at')
        }),
    )
    
    def has_add_permission(self, request):
        return False