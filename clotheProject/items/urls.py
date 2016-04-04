from django.conf.urls import url

from items.models import Item
from items.views import item_view, favorite_item

urlpatterns = [
    url(r'^$', item_view, name="item_view"),
    url(r'^favorites', favorite_item, name="favorite_item"),
    ]
