from django.contrib import admin
from django.urls import path, include

from .views import index, show_wishlist, show_all_wishlists

urlpatterns = [
    path('', index, name='index'),
    path('wishlists/', show_all_wishlists, name='user-wishlists'),
    path('wishlist/<str:slug>/', show_wishlist, name='user-wishlist'),
]
