from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts as dbPosts



def home(request):
    context = {
        'posts': dbPosts.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})