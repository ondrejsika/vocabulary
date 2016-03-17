# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('currency', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('drv_balance', models.FloatField(null=True, blank=True)),
                ('user', models.ForeignKey(related_name='invoice_account_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.FloatField()),
                ('number', models.IntegerField()),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('file', models.FileField(null=True, upload_to='invoice/invoice/file', blank=True)),
                ('label', models.CharField(default='', max_length=255, blank=True)),
                ('drv_balance', models.FloatField(null=True, blank=True)),
                ('account', models.ForeignKey(to='invoice.Account')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
