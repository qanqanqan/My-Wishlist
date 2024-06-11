from django.urls import path

from .views import index, ShowSingleWishlist, ShowWishlists, add_wishlist

urlpatterns = [
    path('', index, name='index'),
    path('wishlists/', ShowWishlists.as_view(), name='user-wishlists'),
    path('wishlist/<str:slug>/', ShowSingleWishlist.as_view(), name='user-wishlist'),
    path('add-wishlist', add_wishlist, name='add-wishlist'),
]
