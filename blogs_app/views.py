from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
    name = request.GET.get("name") or "world"
    #return HttpResponse("Hello, {}!".format(name))
    # return render(request, "blogs_app/base.html")
    return render(request, "blogs_app/base.html", {"name": name})

