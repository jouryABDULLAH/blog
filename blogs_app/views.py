from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
    #name = request.GET.get("name")
    return render(request, "blogs_app/blogs.html")

