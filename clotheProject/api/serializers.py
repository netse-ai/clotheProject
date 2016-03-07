from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from items.models import Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('name', 'price', 'description', 'rating', 'photo')


class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
