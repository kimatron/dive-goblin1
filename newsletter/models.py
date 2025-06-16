"""
Newsletter models for Dive Goblin e-commerce platform.

Handles newsletter subscriptions and email campaign management
for marketing communications with customers.
"""

from django.db import models
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
import uuid


class NewsletterSubscriber(models.Model):
    """
    Model representing newsletter subscribers.
    
    Stores subscriber email addresses, subscription status,
    and unique tokens for unsubscribe functionality.
    """
    
    email = models.EmailField(
        unique=True,
        help_text="Subscriber's email address")
    date_subscribed = models.DateTimeField(
        default=timezone.now,
        help_text="Date and time of subscription")
    is_active = models.BooleanField(
        default=True,
        help_text="Whether subscription is active")
    unsubscribe_token = models.UUIDField(
        default=uuid.uuid4, 
        editable=False, 
        null=True, 
        blank=True,
        help_text="Unique token for unsubscribe links")
    
    def __str__(self):
        """Return the subscriber's email as string representation."""
        return self.email
    
    class Meta:
        ordering = ['-date_subscribed']


class Newsletter(models.Model):
    """
    Model representing newsletter campaigns.
    
    Stores newsletter content and handles bulk email sending
    to all active subscribers with tracking of send status.
    """
    
    subject = models.CharField(
        max_length=200,
        help_text="Newsletter subject line")
    content = models.TextField(
        help_text="Newsletter content (HTML supported)")
    created_at = models.DateTimeField(
        default=timezone.now,
        help_text="Date and time newsletter was created")
    sent_at = models.DateTimeField(
        null=True, 
        blank=True,
        help_text="Date and time newsletter was sent")
    
    def __str__(self):
        """Return the newsletter subject as string representation."""
        return self.subject
    
    def send_newsletter(self):
        """
        Send this newsletter to all active subscribers.
        
        Creates personalized emails with unsubscribe links for each
        active subscriber and tracks successful deliveries.
        
        Returns:
            int: Number of emails successfully sent.
            
        Raises:
            ValueError: If newsletter already sent or no active subscribers.
        """
        if self.sent_at:
            raise ValueError("This newsletter has already been sent")
        
        subscribers = NewsletterSubscriber.objects.filter(is_active=True)
        if not subscribers.exists():
            raise ValueError("No active subscribers to send to")
        
        sent_count = 0
        for subscriber in subscribers:
            try:
                # Create unsubscribe URL with token if available
                if hasattr(subscriber, 'unsubscribe_token') and subscriber.unsubscribe_token:
                    unsubscribe_url = f"{settings.BASE_URL}/newsletter/unsubscribe/{subscriber.unsubscribe_token}/"
                else:
                    unsubscribe_url = f"{settings.BASE_URL}/newsletter/unsubscribe/"
                
                # Render email template
                html_content = render_to_string('newsletter/email_template.html', {
                    'subject': self.subject,
                    'content': self.content,
                    'unsubscribe_url': unsubscribe_url
                })
                
                # Send the email
                send_mail(
                    subject=self.subject,
                    message="Please view this email with an HTML-compatible email client",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[subscriber.email],
                    html_message=html_content,
                    fail_silently=False,
                )
                sent_count += 1
            except Exception as e:
                print(f"Error sending to {subscriber.email}: {e}")
                continue
        
        # Update sent_at timestamp
        self.sent_at = timezone.now()
        self.save()
        
        return sent_count