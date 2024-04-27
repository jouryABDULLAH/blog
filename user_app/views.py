from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import UserSignupForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been created! You are now able to log in.")
            return redirect('user_app/login')  # Redirect to login page after successful signup
    else:
        form = UserSignupForm()
    return render(request, 'user_app/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_app/login')  # Redirect to login page after successful signup
    else:
        form = UserSignupForm()
    return render(request, 'user_app/signup.html', {'form': form})