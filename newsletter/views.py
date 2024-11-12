from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import NewsletterSubscriber, Newsletter
from .forms import NewsletterCreationForm
import json

@require_POST
def newsletter_signup(request):
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
    if request.method == 'POST':
        form = NewsletterCreationForm(request.POST)
        if form.is_valid():
            newsletter = form.save()
            try:
                num_sent = newsletter.send_newsletter()
                messages.success(request, f'Newsletter sent successfully to {num_sent} subscribers!')
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

# newsletter/utils.py
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_welcome_email(subscriber):
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