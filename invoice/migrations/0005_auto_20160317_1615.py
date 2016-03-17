# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_auto_20160317_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='drv_yeat_balance',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='year',
            name='drv_balance',
            field=models.FloatField(default=0, blank=True),
        ),
    ]
