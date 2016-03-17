from django.conf.urls import url

from users.models import UserProfile
from users.views import users_view, user_login, user_profile

urlpatterns = [
    url(r'^$', users_view, name="users_view"),
    url(r'^login', user_login, name="login"),
    url(r'^profile', user_profile, name="profile"),
    ]
