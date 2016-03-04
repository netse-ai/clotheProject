from django.db import models


class Item(models.Model):
    """Item Object Class"""
    name = models.CharField(max_length=125, blank=True)
    price = models.FloatField(default=0, blank=True)
    rating = models.IntegerField(default=0, blank=True)
    description = models.TextField(max_length=300, blank=True)


    def __unicode__(self):
        return unicode(self.name)
