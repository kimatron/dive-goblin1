"""
Profile views for Dive Goblin e-commerce platform.

Handles user profile management, order history, account updates,
and account deletion functionality.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile
from .forms import UserProfileForm, UserInformationForm
from checkout.models import Order
from django.urls import reverse


@login_required
def profile(request):
    """
    Display and handle updates to user profile information.
    
    Handles both delivery information and personal information updates
    via separate forms identified by form_type parameter.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Rendered profile page with forms and order history.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        if request.POST.get('form_type') == 'delivery_form':
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Delivery information updated successfully')
            else:
                messages.error(request, 'Update failed. Please ensure the form is valid.')

        elif request.POST.get('form_type') == 'info_form':
            info_form = UserInformationForm(request.POST, instance=profile)
            if info_form.is_valid():
                info_form.save()
                messages.success(request, 'Profile information updated successfully')
            else:
                messages.error(request, 'Update failed. Please ensure all fields are valid.')

    form = UserProfileForm(instance=profile)
    info_form = UserInformationForm(instance=profile)
    orders = profile.orders.all().order_by('-date')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'info_form': info_form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Display order details from user's order history.
    
    Shows past order confirmation with a note that this is historical data.
    
    Args:
        request (HttpRequest): The HTTP request object.
        order_number (str): The order number to display.
        
    Returns:
        HttpResponse: Rendered checkout success page with order details.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def update_account(request):
    """
    Handle account updates including username, email, and password changes.
    
    Requires current password verification for security. Updates username
    and email if provided, and changes password if new password is given.
    
    Args:
        request (HttpRequest): The HTTP request object containing form data.
        
    Returns:
        HttpResponseRedirect: Redirect to profile page with success/error message.
    """
    if request.method == 'POST':
        user = request.user
        current_password = request.POST.get('current_password')

        if not user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('profiles:profile')

        username = request.POST.get('username')
        email = request.POST.get('email')

        if username and username != user.username:
            user.username = username
        if email and email != user.email:
            user.email = email

        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password:
            if new_password == confirm_password:
                user.set_password(new_password)
                update_session_auth_hash(request, user)
                messages.success(request, 'Password updated successfully.')
            else:
                messages.error(request, 'New passwords do not match.')
                return redirect('profiles:profile')

        user.save()
        messages.success(request, 'Account updated successfully.')
        return redirect('profiles:profile')

    return redirect('profiles:profile')


@login_required
def delete_account(request):
    """
    Handle user account deletion with password verification.
    
    Permanently deletes the user account after password confirmation.
    Logs out the user and redirects to home page upon successful deletion.
    
    Args:
        request (HttpRequest): The HTTP request object containing password.
        
    Returns:
        HttpResponseRedirect: Redirect to home page or profile with message.
    """
    if request.method == 'POST':
        user = request.user
        password = request.POST.get('password')

        # Verify password
        if not user.check_password(password):
            messages.error(request, 'Incorrect password.')
            return redirect('profiles:profile')

        try:
            # Delete the user and log them out
            user.delete()
            logout(request)
            messages.success(request, 'Your account has been deleted.')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Error deleting account: {str(e)}')

    return redirect('profiles:profile')