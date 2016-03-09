from django.contrib.auth.models import User
from django.db import models

from items.models import Item

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True)
    favorites = models.ManyToManyField(Item, blank=True)
    photo = models.ImageField(upload_to='media/', blank=True)
    likes = models.IntegerField(blank=True)
    dislikes = models.IntegerField(blank=True)

    def __unicode__(self):
        return unicode(self.user.username)
