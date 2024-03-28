from django.shortcuts import render,redirect
from .models import post
#from django.http import HttpResponse


def index(request):
    return render(request, "blogs_app/blogs.html")

def new_post(request):
    #name = request.GET.get("name")
    return render(request, "blogs_app/new_post.html")

def my_blogs(request):

    if request.method == "POST":
        post_title = request.POST.get('title')
        post_category = request.POST.get('category')
        post_content = request.POST.get('blog_content')

    my_post = post(title = post_title, category = post_category, content = post_content)

    return render(request, "blogs_app/myblogs.html",  {'post':my_post})
