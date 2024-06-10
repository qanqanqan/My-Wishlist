from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from .models import WishlistPosition, Wishlist


def index(req):
    return render(req, 'wsite/index.html', {'title': 'mytitle'})


def show_all_wishlists(req):
    wishlists = Wishlist.objects.filter(owner=req.user)
    
    context = {
        'title': 'wishlists',
        'wishlists': wishlists,
    }

    return render(req, 'wsite/wishlists-list.html', context)


def show_wishlist(req, slug):
    searchable_wishlist = Wishlist.objects.get(slug=slug)

    if searchable_wishlist.owner != req.user:
        raise PermissionDenied
    
    positions = WishlistPosition.objects.filter(wishlist=searchable_wishlist)

    context = {
        'title': 'wishlist',
        'positions': positions,
    }

    return render(req, 'wsite/wishlist.html', context)
