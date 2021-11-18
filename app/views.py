from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def Home(request):
    context = {
        'blog': BlogPost.objects.get(id=1),
    }
    return render(request, 'index.html', context)