from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_confirmation_email(order):
    """Send the user a confirmation email"""
    # Get the subject from template or use a fixed one
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_email_subject.txt',
        {'order': order}).strip()
    
    # Plain text email body
    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
    
    # HTML email body
    html_body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.html',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
    
    # Send email with HTML content
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [order.email],
        html_message=html_body,
        fail_silently=False,
    )