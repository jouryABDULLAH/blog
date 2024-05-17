from django.shortcuts import render,redirect
from .models import post
#from django.http import HttpResponse


def index(request):
    categories_list = post.objects.values_list('category', flat=True)
    categories_set = set(categories_list)

    if request.method == "POST":
        chosen_category = request.POST.get('category')
        if chosen_category and chosen_category != "all":
            posts = post.objects.filter(category=chosen_category)
        else:
            posts = post.objects.all()
    else:
        posts = post.objects.all()

    return render(request, "blogs_app/blogs.html", {'categories': categories_set, 'posts': posts})

def new_post(request):
    
    categories_list = post.objects.values_list('category', flat=True)
    categories_set = set(categories_list)

    return render(request, "blogs_app/new_post.html", {'categories':categories_set})

def my_blogs(request):

    if request.method == "POST":
        post_title = request.POST.get('title')
        post_category = request.POST.get('category')
        post_content = request.POST.get('blog_content')

    my_post = post(title = post_title, category = post_category, content = post_content)

    return render(request, "blogs_app/myblogs.html",  {'post':my_post})
