from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from api.serializers import ItemSerializer, UserSerializer, UserProfileSerializer
from api.views import *
from api.urls import router
from home import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^items/', include('items.urls', namespace='items')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^', 'home.views.register'
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
