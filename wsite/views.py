from typing import Any
from django.shortcuts import redirect, render
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView
from django.template.defaultfilters import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout

from .models import WishlistPosition, Wishlist
from .forms import *

from .addons import to_latin


def index(req):
    return render(req, 'wsite/index.html', {'title': 'mytitle'})


def authenticate(req):
    if req.user.is_authenticated:
        return redirect('user-wishlists')
    
    if req.method == 'GET':
        form = UserAuthenticationForm()
    else:
        form = UserAuthenticationForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            return redirect('user-wishlists')
    return render(req, 'wsite/login.html', {'form': form})


def register(req):
    if req.user.is_authenticated:
        return redirect('user-wishlists')
    
    if req.method == 'GET':
        form = UserCreationFormC()
    else:
        form = UserCreationFormC(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(req, 'wsite/register.html', {'form': form})

def user_logout(req):
    logout(req)
    return redirect('index')


class ShowWishlists(LoginRequiredMixin, ListView):
    template_name = 'wsite/wishlists-list.html'
    context_object_name = 'wishlists'

    def get_queryset(self):
        return Wishlist.objects.filter(owner=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'wishlists'
        form = CreateWishlistForm()
        context['form'] = form
        return context


class ShowSingleWishlist(LoginRequiredMixin, ListView):
    template_name = 'wsite/wishlist.html'
    context_object_name = 'positions'

    def get_queryset(self):
        searchable_wishlist = Wishlist.objects.get(slug=self.kwargs['slug'])

        if searchable_wishlist.owner != self.request.user:
            raise PermissionDenied
        
        return WishlistPosition.objects.filter(wishlist=searchable_wishlist)
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'wishlist'
        context['form'] = CreateWishlistPositionForm()
        context['slug'] = self.kwargs['slug']
        return context


# WISHLISTS FUNCS
def add_wishlist(req):
    if req.method == 'POST':
        form = CreateWishlistForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            if not data['name']:
                return redirect('user-wishlists')
            Wishlist.objects.create(name=data['name'], slug=slugify(to_latin(data['name'])), owner=req.user)

    return redirect('user-wishlists')


def delete_wishlist(req, slug):
    # wishlist = get_object_or_404(Wishlist, slug=slug)
    wishlist = Wishlist.objects.get(slug=slug)

    if not wishlist:
        redirect('user-wishlists')

    if wishlist.owner != req.user:
        raise PermissionDenied
    
    wishlist.delete()
    return redirect('user-wishlists')


def change_wishlist_publicity(req):
    if req.method != 'POST':
        return redirect('user-wishlists')
    
    data = req.POST
    for key, value in dict(data).items():
        if not key.startswith('wishlist-'):
            continue

        wishlist_pk = int(key[-1])
        bool_val = True if value[0] == 'on' else False
        Wishlist.objects.filter(pk=wishlist_pk).update(public=bool_val)
    
    return redirect('user-wishlists')



# WISHLIST POSITIONS FUNCS
def add_position(req, slug):
    if req.method == 'POST':
        form = CreateWishlistPositionForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            WishlistPosition.objects.create(title=data['title'], description=data['description'], wishlist=Wishlist.objects.get(slug=slug))
    
    return redirect('user-wishlist', slug=slug)


def delete_position(req, pk):
    pos = WishlistPosition.objects.get(pk=pk)

    if not pos:
        redirect('user-wishlists')

    if pos.wishlist.owner != req.user:
        raise PermissionDenied
    
    pos.delete() 
    return redirect('user-wishlist', slug=pos.wishlist.slug)
