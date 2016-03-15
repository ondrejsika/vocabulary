from django.contrib import admin

from spending.models import Tag, Type, Tx, Account



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


admin.site.register(Tag, TagAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Tx, TxAdmin)
admin.site.register(Account, AccountAdmin)
