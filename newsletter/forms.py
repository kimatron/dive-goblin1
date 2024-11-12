from django import forms
from .models import NewsletterSubscriber, Newsletter


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'newsletter-input',
                'placeholder': 'YOUR EMAIL ADDRESS'
            })
        }


class NewsletterCreationForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }
