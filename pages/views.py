from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm


def about_view(request):
    return render(request, 'pages/about.html')


def faq_view(request):
    return render(request, 'pages/faq.html')


def privacy_view(request):
    return render(request, 'pages/privacy.html')


def terms(request):
    return render(request, 'pages/terms.html')


def contact(request):
    if request.method == 'POST':
        # Get data directly from POST
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Basic validation
        if name and email and subject and message:
            try:
                # Email body
                email_body = f"""
                New contact form submission from Dive Goblin:

                Name: {name}
                Email: {email}
                Subject: {subject}
                Message: {message}
                """

                # Send email
                send_mail(
                    f'New Contact Form Submission: {subject}',
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )

                messages.success(request, 'Your message has been sent! We will get back to you soon.')
                
            except Exception as e:
                print(f"Error sending email: {e}")
                messages.error(request, 'Sorry, there was an error sending your message. Please try again later.')
        else:
            messages.error(request, 'Please fill in all fields.')

        return redirect('pages:contact')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})
