# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_auto_20160317_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='fixed_cost_ratio',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='tax_ratio',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
