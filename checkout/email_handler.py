from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_confirmation_email(order):
    """Send the user a confirmation email"""
    subject = f'Dive Goblin - Order Confirmation {order.order_number}'
    
    # Render email text content
    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.html',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
    )
    
    # Send email
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [order.email]
    )