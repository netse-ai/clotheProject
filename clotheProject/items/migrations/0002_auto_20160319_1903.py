# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='photo_url',
            field=models.URLField(blank=True),
        ),
    ]
