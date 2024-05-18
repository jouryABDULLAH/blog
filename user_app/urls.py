from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from user_app import views

app_name = 'user_app'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
]