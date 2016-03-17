# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_auto_20160317_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountyear',
            name='account',
        ),
        migrations.RemoveField(
            model_name='accountyear',
            name='user',
        ),
        migrations.RemoveField(
            model_name='accountyear',
            name='year',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='drv_account_year',
        ),
        migrations.AddField(
            model_name='year',
            name='account',
            field=models.ForeignKey(default=1, to='invoice.Account'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AccountYear',
        ),
    ]
