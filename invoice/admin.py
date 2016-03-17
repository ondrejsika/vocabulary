from django.contrib import admin

from spending.admin import BaseAdmin
from invoice.models import Account, Invoice, Year


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
        'drv_year_balance',
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


class YearAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = (
        'user',
        'year',
        'account',
        lambda x: x.account.currency,
        'drv_balance',
        lambda x: x.drv_balance - (x.drv_balance * x.fixed_cost_ratio) if x.fixed_cost_ratio else '',
        lambda x: (x.drv_balance - (x.drv_balance * x.fixed_cost_ratio)) * x.tax_ratio if x.fixed_cost_ratio and x.tax_ratio else '',
    )

    def formfield_for_foreignkey(self, *args, **kwargs):
        return self.build__formfield_for_foreignkey(YearAdmin)(self, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return self.build__get_queryset(YearAdmin)(self, *args, **kwargs)


admin.site.register(Account, AccountAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Year, YearAdmin)
