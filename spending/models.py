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

    def save(self, *args, **kwargs):
        self.drv_balance = self._get_balance()
        return super(Account, self).save(*args, **kwargs)

    def _get_balance(self):
        tx_sum = Tx.objects.filter(user=self.user, account=self).aggregate(balance=models.Sum('amount'))['balance'] or 0
        return self.start_balance + tx_sum


class Tx(models.Model):
    user = models.ForeignKey('auth.User')

    account = models.ForeignKey(Account)
    type = models.ForeignKey(Type)
    amount = models.FloatField()
    label = models.CharField(max_length=255, default='', blank=True)
    # tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    drv_balance = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return '%s %s, %s - %s' % (self.amount, self.account.currency, self.type, self.label)

    def save(self, *args, **kwargs):
        self.drv_balance = self.account.drv_balance
        ret = super(Tx, self).save(*args, **kwargs)
        self.account.save()
        return ret
