from django.conf.urls import include, url, patterns
from rest_framework import routers, serializers, viewsets
from api.serializers import ItemSerializer, UserSerializer, UserProfileSerializer
from api.views import *

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^$', include(router.urls)),
    url(r'^items/(?P<pk>[0-9]+)/$', include(ItemDetail.as_view())),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
