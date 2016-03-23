from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import UserProfile
from items.models import Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('name', 'price', 'description', 'rating', 'photo', 'barcode', 'photo_url','item_url' )


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('likes', 'dislikes', 'photo')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    userprofile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ('username', 'url', 'email', 'is_staff', 'password', 'userprofile')

    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(**profile_data)
        return user
