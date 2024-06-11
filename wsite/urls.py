from django.urls import path

from .views import index, add_wishlist, ShowSingleWishlist, ShowWishlists, authenticate, user_logout

urlpatterns = [
    path('', index, name='index'),
    path('wishlists/', ShowWishlists.as_view(), name='user-wishlists'),
    path('wishlist/<str:slug>/', ShowSingleWishlist.as_view(), name='user-wishlist'),
    path('add-wishlist', add_wishlist, name='add-wishlist'),
    path('login/', authenticate, name='login'),
    path('logout/', user_logout, name='logout')
]
