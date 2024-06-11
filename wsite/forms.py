from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Wishlist


class CreateWishlistForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'nes-input nes-btn-noborder'}))
    slug = forms.CharField(required=False, widget=forms.HiddenInput())
    owner = forms.CharField(required=False, widget=forms.HiddenInput())


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class UserCreationFormC(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = False

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
