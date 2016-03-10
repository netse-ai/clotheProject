from django.conf.urls import url

from users.models import UserProfile
from users.views import users_view

urlpatterns = [
    url(r'^$', users_view, name="users_view"),
    ]
