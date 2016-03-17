# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0005_auto_20160317_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='fixed_cost_ratio',
        ),
        migrations.RemoveField(
            model_name='account',
            name='tax_ratio',
        ),
    ]
