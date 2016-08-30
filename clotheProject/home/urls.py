from django.conf.urls import url

# from items.models import Item
from home.views import register

urlpatterns = [
    url(r'^$', register, name="index"),
    ]
