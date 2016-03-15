from __future__ import unicode_literals

from django.db import models


class Type(models.Model):
    user = models.ForeignKey('auth.User')

    name = models.CharField(max_length=32)

    def __unicode__(self):
        return '%s' % self.name


class Tag(models.Model):
    user = models.ForeignKey('auth.User')

    name = models.CharField(max_length=32)

    def __unicode__(self):
        return '%s' % self.name


class Account(models.Model):
    user = models.ForeignKey('auth.User')

    name = models.CharField(max_length=32)
    start_balance = models.FloatField(default=0)
    currency = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    drv_balance = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.name


class Tx(models.Model):
    user = models.ForeignKey('auth.User')

    account = models.ForeignKey(Account)
    type = models.ForeignKey(Type)
    amount = models.FloatField()
    label = models.CharField(max_length=255, default='')
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    drv_balance = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return '%s %s, %s - %s' % (self.amount, self.account.currency, self.type, self.label)
