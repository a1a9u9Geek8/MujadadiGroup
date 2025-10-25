from django import forms
from .models import ContactMessage, JobApplication

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'phone', 'company', 'business_unit', 'subject', 'message', 'newsletter']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'business_unit': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('', 'Select Business Unit'),
                ('agriculture', 'Agriculture'),
                ('pharmacy', 'Pharmacy'),
                ('supply-chain', 'Supply Chain'),
                ('logistics', 'Logistics'),
                ('contracting', 'Contracting'),
                ('energy', 'Energy'),
                ('real-estate', 'Real Estate'),
            ]),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'required': True}),
            'newsletter': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email', 'phone', 'position_applied', 'experience_years', 'cover_letter', 'cv_file']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'position_applied': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'experience_years': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '50', 'required': True}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Tell us why you want to join Mujadadi Group...', 'required': True}),
            'cv_file': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.doc,.docx', 'required': True}),
        }