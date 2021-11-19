from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('post/<slug>', views.Post, name='Post'),
    
]