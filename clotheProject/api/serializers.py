from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import UserProfile, Favorites
from items.models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('item_url', 'name', 'price', 'description', 'rating', 'photo', 'photo_url')


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('likes', 'dislikes', 'photo')

class FavoritesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Favorites
        fields = ('userprofile', 'item')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    userprofile = UserProfileSerializer()
    favorites = FavoritesSerializer(many=True)
    class Meta:
        model = User
        fields = ('username', 'url', 'email', 'is_staff', 'password', 'userprofile')

    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile')
        user = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user
