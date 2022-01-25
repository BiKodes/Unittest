from unicodedata import name
from django.contrib import admin
from django.urls import path
from posts.views import home_view, about_view, PostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('posts/', PostView.as_view(), name='posts')
]
