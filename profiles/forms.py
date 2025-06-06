from django import forms
from .models import UserProfile
# from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['default_phone_number', 'default_street_address1',
                  'default_street_address2', 'default_town_or_city',
                  'default_county', 'default_postcode', 'default_country']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Postal Code',
        }

        for field in self.fields:
            if field != 'default_country':
                self.fields[field].widget.attrs['class'] = 'brutal-input'
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class UserInformationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['gender', 'date_of_birth', 'diving_level', 'bio']
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date', 'class': 'brutal-input'}
            ),
            'bio': forms.Textarea(
                attrs={
                    'class': 'brutal-textarea',
                    'placeholder': 'Tell us about yourself...',
                    'rows': 3
                }
            ),
            'gender': forms.Select(attrs={'class': 'brutal-input'}),
            'diving_level': forms.Select(attrs={'class': 'brutal-input'}),
        }