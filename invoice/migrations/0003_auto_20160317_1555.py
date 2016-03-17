# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20160317_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountyear',
            name='drv_balance',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='year',
            name='drv_balance',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
