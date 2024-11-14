from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'brutal-input',
            'placeholder': 'Your Name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'brutal-input',
            'placeholder': 'Your Email'
        })
    )
    subject = forms.CharField(
        min_length=3,
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'brutal-input',
            'placeholder': 'Subject'
        })
    )
    message = forms.CharField(
        min_length=10,
        widget=forms.Textarea(attrs={
            'class': 'brutal-textarea',
            'rows': 5,
            'placeholder': 'Your Message'
        })
    )