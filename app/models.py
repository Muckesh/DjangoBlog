from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=SET_NULL, null=True, blank=True)
    img = models.ImageField(upload_to='images/')
    description = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=600, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
