from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('wishlists/', ShowWishlists.as_view(), name='user-wishlists'),
    path('wishlist/<str:slug>/', ShowSingleWishlist.as_view(), name='user-wishlist'),

    path('add-wishlist/', add_wishlist, name='add-wishlist'),
    path('delete-wishlist/<str:slug>/', delete_wishlist, name='delete-wishlist'),
    
    path('add-position/<str:slug>/', add_position, name='add-position'),
    path('delete-position/<int:pk>/', delete_position, name='delete-position'),

    path('login/', authenticate, name='login'),
    path('logout/', user_logout, name='logout')
]
