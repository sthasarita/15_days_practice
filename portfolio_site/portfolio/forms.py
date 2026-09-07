from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com', 'class': 'form-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message...', 'class': 'form-input', 'rows': 5}),
        }