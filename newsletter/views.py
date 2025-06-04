from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from .models import NewsletterSubscriber
from .forms import NewsletterCreationForm

import json


@require_POST
def newsletter_signup(request):
    """Handle AJAX requests for newsletter sign-ups."""
    try:
        data = json.loads(request.body)
        email = data.get('email', '').strip()
        
        print(f"DEBUG: Email received: '{email}'")
        print(f"DEBUG: Email length: {len(email)}")
        print(f"DEBUG: Email type: {type(email)}")

        validate_email(email)
        print(f"DEBUG: Email validation passed")

        # Add detailed database check
        existing_count = NewsletterSubscriber.objects.filter(email=email).count()
        print(f"DEBUG: Existing subscribers with this email: {existing_count}")
        
        if existing_count > 0:
            print(f"DEBUG: Found existing subscriber(s)")
            existing_subs = NewsletterSubscriber.objects.filter(email=email)
            for sub in existing_subs:
                print(f"DEBUG: Existing subscriber: '{sub.email}' (ID: {sub.id})")
        
        if NewsletterSubscriber.objects.filter(email=email).exists():
            # Already subscribed - return error toast
            print("DEBUG: Email already exists, rendering error template")
            
            toast_html = render_to_string('includes/toasts/newsletter_error.html')
            
            response_data = {
                'status': 'info',
                'message': "You're already subscribed!",
                'toast_html': toast_html
            }
            
            print(f"DEBUG: Returning 'already exists' response")
            return JsonResponse(response_data)

        print(f"DEBUG: Email does NOT exist, creating new subscriber")
        subscriber = NewsletterSubscriber.objects.create(email=email)
        print(f"DEBUG: NEW SUBSCRIBER CREATED with ID: {subscriber.id}")

        # Send welcome email (if email settings are configured)
        try:
            send_welcome_email(subscriber)
            print(f"DEBUG: Welcome email sent successfully")
        except Exception as e:
            print(f"DEBUG: Failed to send welcome email: {e}")

        # Success - return success toast
        print(f"DEBUG: Rendering SUCCESS template")
        toast_html = render_to_string('includes/toasts/newsletter_success.html', {
            'message': 'Successfully subscribed! Welcome aboard! 🎉'
        })
        
        response_data = {
            'status': 'success',
            'message': 'Successfully subscribed! Welcome aboard! 🎉',
            'toast_html': toast_html
        }
        
        print(f"DEBUG: Returning SUCCESS response")
        return JsonResponse(response_data)

    except ValidationError as e:
        print(f"DEBUG: Email validation failed: {e}")
        toast_html = render_to_string('includes/toasts/newsletter_error.html', {
            'message': 'Please enter a valid email address.'
        })
        return JsonResponse({
            'status': 'error',
            'message': 'Please enter a valid email address.',
            'toast_html': toast_html
        }, status=400)
    except Exception as e:
        print(f"DEBUG: Unexpected error: {e}")
        toast_html = render_to_string('includes/toasts/newsletter_error.html', {
            'message': 'Oops! Something went wrong. Please try again.'
        })
        return JsonResponse({
            'status': 'error',
            'message': 'Oops! Something went wrong. Please try again.',
            'toast_html': toast_html
        }, status=500)
        


@staff_member_required
def create_newsletter(request):
    """
    Handle the creation and sending of a new newsletter.

    Allows staff members to create and send a newsletter to all
    subscribers via a form. If valid, sends the newsletter and
    displays a success message with the number of emails sent.

    Args:
        request (HttpRequest): The request object,\
        including POST data if submitted.

    Returns:
        HttpResponse: Renders the newsletter creation template or redirects
                    with success/error messages\
                    based on the operation's outcome.
    """
    if request.method == 'POST':
        form = NewsletterCreationForm(request.POST)
        if form.is_valid():
            newsletter = form.save()
            try:
                num_sent = newsletter.send_newsletter()
                messages.success(
                    request,
                    f'Newsletter sent successfully to {num_sent} subscribers!')
                return redirect('admin:index')
            except Exception as e:
                messages.error(request, f'Error sending newsletter: {str(e)}')
    else:
        form = NewsletterCreationForm()

    return render(request, 'newsletter/create_newsletter.html', {'form': form})


def unsubscribe(request, token):
    try:
        subscriber = NewsletterSubscriber.objects.get(unsubscribe_token=token)
        subscriber.is_active = False
        subscriber.save()
        messages.success(request, 'You have been successfully unsubscribed.')
    except NewsletterSubscriber.DoesNotExist:
        messages.error(request, 'Invalid unsubscribe link.')

    return render(request, 'newsletter/unsubscribe.html')


def send_welcome_email(subscriber):
    """
    Send a welcome email to a new newsletter subscriber.

    Args:
        subscriber (Subscriber): The subscriber object containing the
                                 subscriber's email address.

    Generates a welcome email using a pre-defined HTML template and sends it
    to the subscriber's email address. Includes an unsubscribe link.
    """
    subject = 'Welcome to Dive Goblin Newsletter!'

    # Construct a unique unsubscribe URL for each subscriber
    unsubscribe_url = f"{
        settings.BASE_URL}/newsletter/unsubscribe/{
            subscriber.unsubscribe_token}/"

    html_content = render_to_string('newsletter/welcome_email.html', {
        'unsubscribe_url': unsubscribe_url
    })

    # Attempt to send the email
    send_mail(
        subject=subject,
        message='',
        html_message=html_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[subscriber.email],
        fail_silently=False,
    )
