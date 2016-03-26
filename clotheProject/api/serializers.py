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
        exclude = ('id', 'user')


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('likes', 'dislikes', 'photo', 'tmp_password')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    userprofile = UserProfileSerializer()
    favorite = FavoriteSerializer()
    class Meta:
        model = User
        fields = (
                'id', 'username', 'url',
                 'email', 'is_staff', 'password',
                 'userprofile', 'favorite'
                 )

    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile')
        favorites_data = validated_data.pop('favorite')
        print favorites_data
        user = User.objects.create_user(**validated_data)
        user_profile = UserProfile.objects.create(user=user, **profile_data)
        favorite = Favorite(user=user)
        favorite.save()
        print favorite.items
        # for value in favorites_data:
        #     item = Item.objects.get_or_create(**value)
        for key in favorites_data:
            print key
            for item in favorites_data[key]:
                print item.id
                favorite.items.add(item)
        print favorite.items
        return user

    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('userprofile')
    #     instance.likes = profile_data.get('likes')
    #     instance.dislikes = profile_data.get('dislikes')
    #     instance.photo = profile_data.get('photo')
    #     instance.save()
    #     return instance
    #
    # def create(self, validated_data):
    #     validated_data.pop('userprofile')
    #     user = User.objects.create(**validated_data)
    #     return user
