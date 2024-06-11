from django import forms

from .models import Wishlist


class CreateWishlistForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'nes-input nes-btn-noborder'}))
    slug = forms.CharField(required=False, widget=forms.HiddenInput())
    owner = forms.CharField(required=False, widget=forms.HiddenInput())
