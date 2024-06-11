from django.shortcuts import redirect, render
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView
from django.template.defaultfilters import slugify

from .models import WishlistPosition, Wishlist
from .forms import CreateWishlistForm


def index(req):
    return render(req, 'wsite/index.html', {'title': 'mytitle'})


def add_wishlist(req):
    if req.method == 'POST':
        form = CreateWishlistForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            if not data['name']:
                return redirect('user-wishlists')
            Wishlist.objects.create(name=data['name'], slug=slugify(data['name']), owner=req.user)

    return redirect('user-wishlists')


class ShowWishlists(ListView):
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


class ShowSingleWishlist(ListView):
    template_name = 'wsite/wishlist.html'
    context_object_name = 'positions'
    extra_context = {'title': 'wishlist'}

    def get_queryset(self):
        searchable_wishlist = Wishlist.objects.get(slug=self.kwargs['slug'])

        if searchable_wishlist.owner != self.request.user:
            raise PermissionDenied
        
        return WishlistPosition.objects.filter(wishlist=searchable_wishlist)
