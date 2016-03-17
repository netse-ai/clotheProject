# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dislikes',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='favorites',
            field=models.ManyToManyField(to='items.Item', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='likes',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'media/', blank=True),
        ),
    ]
