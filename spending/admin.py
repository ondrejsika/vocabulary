from django.utils.translation import ugettext_lazy
from django.contrib import admin

from spending.models import Tag, Type, Tx, Account


class MyAdminSite(admin.AdminSite):
    site_title = ugettext_lazy('Spending')
    site_header = ugettext_lazy('Spending')
    index_title = ugettext_lazy('Spending admininstration')


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
    )
    list_filter = (
        'user',
    )


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
    )
    list_filter = (
        'user',
    )


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'drv_balance',
        'currency',
        'created_at',
    )
    list_filter = (
        'user',
        'currency',
        'created_at',
    )

class TxAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'account',
        lambda x: x.account.currency,
        'amount',
        'drv_balance',
        'created_at',
        'type',
        'label',
    )
    list_filter = (
        'user',
        'account',
        'account__currency',
        'created_at',
        'type',
    )

admin_site = MyAdminSite()

admin_site.register(Tag, TagAdmin)
admin_site.register(Type, TypeAdmin)
admin_site.register(Tx, TxAdmin)
admin_site.register(Account, AccountAdmin)
