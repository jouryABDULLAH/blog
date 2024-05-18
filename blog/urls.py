import blogs_app.views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user_app.urls', namespace='user_app')), 
    path('', include('blogs_app.urls', namespace='blogs_app')),
]
