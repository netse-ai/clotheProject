# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0005_auto_20160327_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('items', models.ManyToManyField(to='items.Item')),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
