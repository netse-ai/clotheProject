from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers, serializers, viewsets
from api.serializers import (ItemSerializer, ItemViewSet,
    UserSerializer,
    UserViewSet,
    UserProfileSerializer,
    UserProfileViewSet)



router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'users', UserViewSet)
router.register(r'user_profiles', UserProfileViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^items/', include('items.urls', namespace='items')),
    url(r'^userprofile/', include('users.urls', namespace='userprofile'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
