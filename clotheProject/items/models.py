import random
from django.db import models
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string

class Item(models.Model):
    """Item Object Class"""
    name = models.CharField(max_length=125, blank=True)
    price = models.FloatField(default=0, blank=True)
    rating = models.IntegerField(default=0, blank=True)
    description = models.TextField(max_length=300, blank=True)
    photo = models.ImageField(upload_to="media/", blank=True)
    photo_url = models.URLField(max_length=200, blank=True)
    # identifier = models.IntegerField(default=0, blank=False)


    def __unicode__(self):
        return unicode(self.name)


#
#
# def create_unique_identifier(sender, instance, created, **kwargs):
#     if created:
#         idu = random.randrange(0, 100000)
#         Item.objects.create(identifier=idu)
#
# post_save.connect(create_unique_identifier, sender=Item)
