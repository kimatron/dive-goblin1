from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    Extended user profile model for storing additional user information.
    Stores diving-specific user preferences, contact details, and
    default shipping information for the e-commerce platform.
    One-to-one relationship with Django's built-in User model.
    """
    GENDER_CHOICES = [
        ('', 'Prefer not to say'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    DIVING_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('professional', 'Professional'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        help_text="Link to Django's built-in User model")
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
        help_text="User's gender preference (optional)")
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        help_text="User's date of birth for age verification")
    diving_level = models.CharField(
        max_length=20,
        choices=DIVING_LEVEL_CHOICES,
        blank=True,
        null=True,
        help_text="User's diving experience level")
    bio = models.TextField(
        blank=True,
        null=True,
        help_text="User's personal bio/description")
    default_phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text="Default phone number for orders")
    default_street_address1 = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        help_text="Default street address line 1")
    default_street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        help_text="Default street address line 2")
    default_town_or_city = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        help_text="Default city for shipping")
    default_county = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        help_text="Default county/state for shipping")
    default_postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text="Default postal/zip code")
    default_country = CountryField(
        blank_label='Country',
        null=True,
        blank=True,
        help_text="Default country for shipping")

    def __str__(self):
        """Return the username as string representation."""
        return self.user.username

    def get_full_address(self):
        """
        Return formatted full address string.
        Returns:
            str: Complete address or 'No address provided' if incomplete.
        """
        if self.default_street_address1 and self.default_town_or_city:
            address_parts = [
                self.default_street_address1,
                self.default_street_address2,
                self.default_town_or_city,
                self.default_county,
                self.default_postcode,
                str(self.default_country) if self.default_country else None
            ]
            return ', '.join(part for part in address_parts if part)
        return 'No address provided'

    def is_diving_profile_complete(self):
        """
        Check if diving-related profile information is complete.

        Returns:
            bool: True if diving level and bio are provided.
        """
