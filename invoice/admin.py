from django.contrib import admin

from spending.admin import BaseAdmin
from invoice.models import Account, Invoice


class AccountAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'drv_balance',
        'currency',
        'created_at',
    )
    list_filter = (
        # 'user',
        'currency',
        'created_at',
    )

    def formfield_for_foreignkey(self, *args, **kwargs):
        return self.build__formfield_for_foreignkey(AccountAdmin)(self, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return self.build__get_queryset(AccountAdmin)(self, *args, **kwargs)


class InvoiceAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = (
        'user',
        'account',
        'number',
        lambda x: x.account.currency,
        'amount',
        'drv_balance',
        'created_at',
        'label',
        lambda x: x.file.name.split('/')[-1],
    )
    list_filter = (
        # 'user',
        # 'account',
        # 'account__currency',
        'created_at',
        # 'type',
    )

    def formfield_for_foreignkey(self, *args, **kwargs):
        return self.build__formfield_for_foreignkey(InvoiceAdmin)(self, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return self.build__get_queryset(InvoiceAdmin)(self, *args, **kwargs)


admin.site.register(Account, AccountAdmin)
admin.site.register(Invoice, InvoiceAdmin)
