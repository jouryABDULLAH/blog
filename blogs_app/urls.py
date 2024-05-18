from django.contrib import admin
from django.urls import path, include
from blogs_app import views

app_name = 'blogs_app'

urlpatterns = [
    path('', views.index),
    path('new_post', views.new_post, name='categories'),
    path('my_blogs',views.my_blogs, name='post'),
]