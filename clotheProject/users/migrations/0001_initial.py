# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(null=True, upload_to=b'media/', blank=True)),
                ('likes', models.IntegerField(null=True, blank=True)),
                ('dislikes', models.IntegerField(null=True, blank=True)),
                ('favorites', models.ManyToManyField(to='items.Item', blank=True)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
