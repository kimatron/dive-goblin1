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
    """
    Handle AJAX requests for newsletter sign-ups.

    Receives JSON data containing an email address, validates it, and
    checks if the email is already subscribed. If valid and new, adds the
    email to the NewsletterSubscriber database and sends a welcome email.

    Args:
        request (HttpRequest): The request object containing the JSON payload.

    Returns:
        JsonResponse: A JSON response indicating the status of the subscription
                      (success, info if already subscribed, or error for
                      invalid email).
    """
    try:
        data = json.loads(request.body)
        email = data.get('email', '').strip()

        validate_email(email)

        if NewsletterSubscriber.objects.filter(email=email).exists():
            return JsonResponse({
                'status': 'info',
                "message": "You're already subscribed!"
            })

        subscriber = NewsletterSubscriber.objects.create(email=email)

        # Send welcome email (if email settings are configured)
        try:
            send_welcome_email(subscriber)
        except Exception as e:
            print(f"Failed to send welcome email: {e}")

        return JsonResponse({
            'status': 'success',
            'message': 'Successfully subscribed! Welcome aboard! 🎉'
        })

    except ValidationError:
        return JsonResponse({
            'status': 'error',
            'message': 'Please enter a valid email address.'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': 'Oops! Something went wrong. Please try again.'
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

    Generates a welcome email using a pre-defined HTML template and sends it\
    to the subscriber's email address. Includes an unsubscribe link.
    """
    subject = 'Welcome to Dive Goblin Newsletter!'
    html_content = render_to_string('newsletter/welcome_email.html', {
        'unsubscribe_url': settings.BASE_URL + '/newsletter/unsubscribe/'
    })

    send_mail(
        subject=subject,
        message='',
        html_message=html_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[subscriber.email],
        fail_silently=False,
    )