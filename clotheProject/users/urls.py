from django.conf.urls import url

from users.models import UserProfile
from users.views import user_profile_view

urlpatterns = [
    url(r'^$', user_profile_view, name="user_profile_view"),
    ]
