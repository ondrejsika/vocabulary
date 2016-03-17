# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_auto_20160317_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='drv_yeat_balance',
            new_name='drv_year_balance',
        ),
    ]
