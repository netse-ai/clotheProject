from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from users.models import UserProfile
from items.models import Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('name', 'price', 'description', 'rating', 'photo', 'photo_url')


class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('user', 'likes', 'dislikes', 'photo', 'favorites')


class UserProfileViewSet(viewsets.ModelViewSet):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
