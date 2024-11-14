from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile
from .forms import UserProfileForm, UserUpdateForm
from django.urls import reverse


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def update_account(request):
    """Update user account information"""
    if request.method == 'POST':
        user = request.user
        current_password = request.POST.get('current_password')

        # Verify current password
        if not user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('profiles:profile')

        # Update username and email
        username = request.POST.get('username')
        email = request.POST.get('email')

        if username and username != user.username:
            user.username = username
        if email and email != user.email:
            user.email = email

        # Update password if provided
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password:
            if new_password == confirm_password:
                user.set_password(new_password)
                update_session_auth_hash(request, user)  # Keep user logged in
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
    """Delete user account"""
    if request.method == 'POST':
        user = request.user
        password = request.POST.get('password')
        confirm_delete = request.POST.get('confirm_delete')

        # Verify password and confirmation
        if not user.check_password(password):
            messages.error(request, 'Incorrect password.')
            return redirect('profiles:profile')

        if not confirm_delete:
            messages.error(request, 'Please confirm account deletion.')
            return redirect('profiles:profile')

        try:
            # Delete the user account
            user.delete()
            messages.success(request, 'Your account has been deleted.')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Error deleting account: {str(e)}')
            return redirect('profiles:profile')

    return redirect('profiles:profile')
