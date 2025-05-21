from django.db import models
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import send_mass_mail
from django.conf import settings
import uuid


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    unsubscribe_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-date_subscribed']


class Newsletter(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

    def send_newsletter(self):
        if self.sent_at:
            raise ValueError("This newsletter has already been sent")

        subscribers = NewsletterSubscriber.objects.filter(is_active=True)

        emails = []
        for subscriber in subscribers:
            # Create a personalized unsubscribe URL for each subscriber
            unsubscribe_url = f"{settings.BASE_URL}/newsletter/unsubscribe/{subscriber.unsubscribe_token}/"
            
            # Render the email template with the personalized unsubscribe URL
            html_content = render_to_string('newsletter/email_template.html', {
                'subject': self.subject,
                'content': self.content,
                'unsubscribe_url': unsubscribe_url
            })

            email = (
                self.subject,
                '',  # Empty string for text content (we're using HTML only)
                html_content,
                settings.DEFAULT_FROM_EMAIL,
                [subscriber.email],
            )
            emails.append(email)

        send_mass_mail(emails, fail_silently=False)

        self.sent_at = timezone.now()
        self.save()

        return len(emails)
