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
        user = super(UserSerializer, self).create(validated_data)
        self.create_or_update_profile(instance, profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', None)
        self.create_or_update_profile(instance, profile_data)
        return super(UserSerializer, self).update(instance, validated_data)

    def create_or_update_profile(self, user, profile_data):
        profile, created = UserProfile.objects.get_or_create(user=user, defaults=profile_data)
        if not created and profile_data is not None:
            super(UserSerializer, self).update(profile, profile_data)
