from django.contrib import admin
from django.urls import path, include

from .views import index, show_wishlist

urlpatterns = [
    path('', index, name='index'),
    path('my-wishlist/', show_wishlist, name='user-wishlist'),
]
