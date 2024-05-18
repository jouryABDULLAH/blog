from django.shortcuts import render,redirect, get_object_or_404
from .models import post
#from django.http import HttpResponse


def index(request):
    categories_list = post.objects.values_list('category', flat=True)
    categories_set = set(categories_list)

    selected_category = request.POST.get('category', 'all')
    if selected_category == 'all':
        posts = post.objects.all()
    else:
        posts = post.objects.filter(category=selected_category)

    return render(request, 'blogs_app/blogs.html', {
        'categories': categories_set,
        'posts': posts,
        'selected_category': selected_category,
    })


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

def post_detail(request, post_id):
    user_post = get_object_or_404(post, id=post_id)
    print(user_post)
    return render(request, 'blogs_app/post_detailes.html', {'post': user_post})