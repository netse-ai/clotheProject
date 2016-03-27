# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20160325_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='items',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='user',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
