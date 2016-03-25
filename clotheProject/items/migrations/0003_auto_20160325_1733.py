# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='items',
            field=models.ManyToManyField(to='items.Item'),
        ),
    ]
