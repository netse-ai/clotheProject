# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160309_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='favorites',
            field=models.ManyToManyField(to='items.Item', blank=True),
        ),
    ]
