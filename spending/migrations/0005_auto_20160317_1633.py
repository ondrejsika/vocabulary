# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0004_auto_20160317_1349'),
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
