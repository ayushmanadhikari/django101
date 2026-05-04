from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts as dbPosts

posts = [
    {
        'title': 'Blog Post 1',
        'content': 'First post content',
        'author': 'Ayusman',
        'date_posted': 'June 1, 2024'
    },
    {
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'author': 'Ashesh',
        'date_posted': 'June 15, 2025'
    },
    {
        'title': 'Blog Post 3',
        'content': 'Second post content',
        'author': 'Ashesh',
        'date_posted': 'June 15, 2025'
    },
    {
        'title': 'Blog Post 4',
        'content': 'Fourth post content',
        'author': 'Ayusman',
        'date_posted': 'June 20, 2025'
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})