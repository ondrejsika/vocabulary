# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0002_auto_20160315_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 15, 20, 48, 40, 973770), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tx',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 15, 20, 48, 52, 846441), auto_now_add=True),
            preserve_default=False,
        ),
    ]
