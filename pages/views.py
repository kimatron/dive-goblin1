from django.shortcuts import render


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
        # Add your form handling logic here
        # You might want to send an email or save to database
        messages.success(request, 'Your message has been sent! We will get back to you soon.')
        return redirect('pages:contact')
    return render(request, 'pages/contact.html')
