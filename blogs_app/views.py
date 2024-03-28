from django.shortcuts import render,redirect
from .models import post
#from django.http import HttpResponse


def index(request):
    return render(request, "blogs_app/blogs.html")

def new_post(request):
    #name = request.GET.get("name")
    return render(request, "blogs_app/new_post.html")
