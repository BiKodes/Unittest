from re import template
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

def home_view(request):
    return render(request, 'home.html', {})

def about_view(request):
    return render(request, 'about.html', {})

class PostView(ListView):
    model = Post
    template_name = 'posts.html'