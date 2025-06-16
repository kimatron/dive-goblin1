"""
Pages views for Dive Goblin e-commerce platform.

Handles static page rendering and contact form functionality
including about, FAQ, privacy policy, terms of service, and contact pages.
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm


def about_view(request):
    """
    Render the about page with company information.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Rendered about page template.
    """
    return render(request, 'pages/about.html')


def faq_view(request):
    """
    Render the frequently asked questions page.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Rendered FAQ page template.
    """
    return render(request, 'pages/faq.html')


def privacy_view(request):
    """
    Render the privacy policy page.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Rendered privacy policy template.
    """
    return render(request, 'pages/privacy.html')


def terms(request):
    """
    Render the terms of service page.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Rendered terms of service template.
    """
    return render(request, 'pages/terms.html')


def contact(request):
    """
    Handle contact form display and submission.
    
    On GET: Display empty contact form.
    On POST: Process form data, send email to admin, and show success/error message.
    
    Args:
        request (HttpRequest): The HTTP request object containing form data.
        
    Returns:
        HttpResponse: Rendered contact page or redirect after form submission.
    """
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