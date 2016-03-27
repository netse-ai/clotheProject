from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating', 'description')

# class FavoritesAdmin(admin.ModelAdmin):
#     list_display = ('user', 'admin_names')

admin.site.register(Item, ItemAdmin)
# admin.site.register(Favorite, FavoritesAdmin)
