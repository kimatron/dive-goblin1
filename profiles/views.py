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
    if request.method == 'POST':
        user = request.user
        password = request.POST.get('password')
        confirm_delete = request.POST.get('confirm_delete')

        if not user.check_password(password):
            messages.error(request, 'Incorrect password.')
            return redirect('profiles:profile')

        if not confirm_delete:
            messages.error(request, 'Please confirm account deletion.')
            return redirect('profiles:profile')

        try:
            user.delete()
            messages.success(request, 'Your account has been deleted.')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Error deleting account: {str(e)}')
            return redirect('profiles:profile')

    return redirect('profiles:profile')