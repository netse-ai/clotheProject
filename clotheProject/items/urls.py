from django.conf.urls import url

from items.models import Item
from items.views import item_view

urlpatterns = [
    url(r'^$', item_view, name="item_view"),
    ]
