# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import invoice.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account', models.ForeignKey(to='invoice.Account')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.IntegerField(default=invoice.models._get_invoice_default_number),
        ),
        migrations.AddField(
            model_name='accountyear',
            name='year',
            field=models.ForeignKey(to='invoice.Year'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='drv_account_year',
            field=models.ForeignKey(blank=True, to='invoice.AccountYear', null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='drv_year',
            field=models.ForeignKey(blank=True, to='invoice.Year', null=True),
        ),
    ]
