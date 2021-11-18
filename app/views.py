from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    context = {
        
    }
    return render(request, 'index.html', context)