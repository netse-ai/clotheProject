from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating', 'description')

admin.site.register(Item, ItemAdmin)
