# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_item_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(upload_to=b'media/', blank=True),
        ),
    ]
