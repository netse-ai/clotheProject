from django.contrib.auth.models import User
from django.db import models

from items.models import Item


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True)
    favorites = models.ForeignKey(Item, blank=True, null=True)
    # comments = models.ForeignKey('comments.Comment', related_name="user_profile_comments", null=True)
    photo = models.ImageField(upload_to='media/', blank=True)
    likes = models.IntegerField(blank=True)
    dislikes = models.IntegerField(blank=True)

    def __unicode__(self):
        return unicode(self.user.username)
