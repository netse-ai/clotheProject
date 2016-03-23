from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from items.models import Item

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True)
    Favorites = models.ManyToManyField(Item)
    photo = models.ImageField(upload_to='media/', blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    dislikes = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.user.username)

#
class Favorites(models.Model):
    pass
#     userprofile = models.OneToOneField(UserProfile, null=True)
#     item = models.ManyToManyField(Item)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
