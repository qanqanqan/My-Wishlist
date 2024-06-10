from django.contrib import admin

from .models import Wishlist, WishlistPosition


class WishlistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(WishlistPosition)
admin.site.register(Wishlist, WishlistAdmin)
