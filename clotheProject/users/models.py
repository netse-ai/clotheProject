from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from items.models import Item

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, null=True)
    # favorites = models.ManyToManyField(Item)
    tmp_password = models.CharField(max_length=32)
    photo = models.ImageField(upload_to='media/', blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    dislikes = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.user.username)

    # def save(self, *args, **kwargs):
    #     if self.photo:
    #         size = (400, 400)
    #         if not self.id and not self.photo:
    #             return
    #
    #         super(UserProfile, self).save(*args, **kwargs)
    #         image = Image.open(self.photo)
    #         image = image.resize(size, Image.ANTIALIAS)
    #         image.save(self.photo.path)
#
# class Favorites(models.Model):
#     pass
#     userprofile = models.OneToOneField(UserProfile, null=True)
#     item = models.ManyToManyField(Item)
#
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#
# post_save.connect(create_user_profile, sender=User)
