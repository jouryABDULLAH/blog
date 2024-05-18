from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, UserLoginForm
from blogs_app.models import post
from django.utils import timezone


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been created! You are now able to log in.")
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserSignupForm()
    return render(request, 'user_app/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('profile')  # Redirect to the profile page after login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'user_app/login.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    user_posts = post.objects.filter(written_by_id=user)

    context = {
        'user': user,
        'user_posts': user_posts,
    }
    return render(request, 'user_app/profile.html', context)