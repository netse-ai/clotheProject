import random
from PIL import Image
from django.db import models
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User


class Item(models.Model):
    """Item Object Class"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125, blank=True)
    price = models.FloatField(default=0, blank=True)
    rating = models.IntegerField(default=0, blank=True)
    description = models.TextField(max_length=300, blank=True)
    photo = models.ImageField(upload_to="media/", blank=True)
    barcode = models.CharField(max_length=20, blank=True)
    photo_url = models.URLField(max_length=200, blank=True)
    item_url = models.URLField(max_length=200, blank=True)

    def __unicode__(self):
        return unicode(self.name)

    def save(self, size=(400,600)):
        if not self.id and not self.photo:
            return

        super(Item, self).save()
        image = Image.open(self.photo)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.photo.path)


class Favorite(models.Model):
    user = models.OneToOneField(User, null=True)
    items = models.ManyToManyField(Item)

    def __unicode__(self):
        return unicode(self.user.username)

    def admin_names(self):
        return '\n'.join([a.name for a in self.items.all()])



#
#
# def create_unique_identifier(sender, instance, created, **kwargs):
#     if created:
#         idu = random.randrange(0, 100000)
#         Item.objects.create(identifier=idu)
#
# post_save.connect(create_unique_identifier, sender=Item)
