# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20160304_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(upload_to=b'/media/', blank=True),
        ),
    ]
