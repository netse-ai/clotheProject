# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20160307_1741'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favorites',
            field=models.ForeignKey(blank=True, to='items.Item', null=True),
        ),
    ]
