# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0003_auto_20160315_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tx',
            name='tags',
        ),
        migrations.AlterField(
            model_name='tx',
            name='label',
            field=models.CharField(default='', max_length=255, blank=True),
        ),
    ]
