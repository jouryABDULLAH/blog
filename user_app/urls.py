from django.contrib import admin
from django.urls import path, include

from user_app import views

urlpatterns = [
    path('', views.index),
]