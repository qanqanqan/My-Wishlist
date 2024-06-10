from django.db import models
from django.contrib.auth.models import User


class Wishlist(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class WishlistPosition(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    links = models.JSONField(default=list, blank=True)
    image = models.ImageField(upload_to='positions/%Y/%m/%d/', blank=True)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
