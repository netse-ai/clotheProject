from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import UserProfile
from items.models import Item, Favorite



class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'description', 'rating', 'photo', 'barcode', 'photo_url','item_url' )


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'user', 'items')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        item_data = validated_data.pop('items')
        user = User.objects.get(id=22)
        favorite, data = Favorite.objects.get_or_create(user=user)
        favorite.save()
        for item in item_data:
            favorite.items.add(item)
        return favorite


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('likes', 'dislikes', 'photo', 'tmp_password')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    userprofile = UserProfileSerializer()
    class Meta:
        model = User
        fields = (
                'id', 'username', 'url',
                 'email', 'is_staff', 'password',
                 'userprofile'
                 )

    def create(self, validated_data):
        print validated_data
        profile_data = validated_data.pop('userprofile')
        user = User.objects.create_user(**validated_data)
        user_profile = UserProfile.objects.get_or_create(user=user, **profile_data)
        user.save()
        return user

    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('userprofile')
    #     instance.likes = profile_data.get('likes')wwww
    #     instance.dislikes = profile_data.get('dislikes')
    #     instance.photo = profile_data.get('photo')
    #     instance.save()
    #     return instance
    #     instance.save()
    #     return instance
