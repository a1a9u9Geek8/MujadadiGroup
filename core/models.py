from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    hero_image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="services")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="gallery")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Galleries"
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return f"{self.category.name} - {self.title}"


class HeroImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hero/')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    head_office = models.TextField()
    annex_office = models.TextField(blank=True)
    phone_numbers = models.TextField(help_text="Separate multiple numbers with |")
    email = models.EmailField()
    instagram = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return "Contact Information"

    def get_phone_list(self):
        return [phone.strip() for phone in self.phone_numbers.split('|') if phone.strip()]


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    business_unit = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    newsletter = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"


class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    is_sent = models.BooleanField(default=False)
    recipients_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_subscribers(self):
        return ContactMessage.objects.filter(newsletter=True).values_list('email', flat=True).distinct()


class TeamMember(models.Model):
    POSITION_CHOICES = [
        ('executive', 'Executive'),
        ('management', 'Management'),
        ('staff', 'Staff'),
        ('advisor', 'Advisor'),
    ]
    
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=POSITION_CHOICES, default='staff')
    bio = models.TextField(max_length=300)
    image = models.ImageField(upload_to='team/')
    linkedin = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    joined_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} - {self.position}"


class JobApplication(models.Model):
    POSITION_CHOICES = [
        ('agriculture', 'Agriculture'),
        ('pharmacy', 'Pharmacy & Labs'),
        ('supply-chain', 'Supply Chain'),
        ('logistics', 'Logistics'),
        ('contracting', 'Contracting'),
        ('energy', 'Energy'),
        ('real-estate', 'Real Estate'),
        ('general', 'General/Any Department'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    position_applied = models.CharField(max_length=50, choices=POSITION_CHOICES)
    experience_years = models.PositiveIntegerField()
    cover_letter = models.TextField(max_length=1000)
    cv_file = models.FileField(upload_to='applications/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_position_applied_display()}"
