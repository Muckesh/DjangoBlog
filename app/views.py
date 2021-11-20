from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.


def Home(request):
    context = {
        'blogs': BlogPost.objects.all().order_by('-date'),
        'category': Category.objects.all(),
    }
    return render(request, 'home.html', context)


def Post(request, slug):
    context = {
        'blog': BlogPost.objects.get(slug=slug)
    }
    return render(request, 'index.html', context)
