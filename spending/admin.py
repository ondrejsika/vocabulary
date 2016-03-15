from django.contrib import admin

from spending.models import Tag, Type, Tx, Account


class BaseAdmin(object):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True
        return obj.user == request.user

    @staticmethod
    def build__formfield_for_foreignkey(cls):
        def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
            field = super(cls, self).formfield_for_foreignkey(db_field, request, **kwargs)
            if db_field.name in ('user', 'account', 'type', 'tags'):
                if not request.user.is_superuser:
                    if db_field.name == 'user':
                        field.queryset = field.queryset.filter(id=request.user.id)
                    else:
                        field.queryset = field.queryset.filter(user=request.user)
            return field
        return formfield_for_foreignkey

    @staticmethod
    def build__get_queryset(cls):
        def get_queryset(self, request):
            return super(cls, self).get_queryset(request).filter(user=request.user)
        return get_queryset


class TagAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = (
        'user',
        'name',
    )
    list_filter = (
        # 'user',
    )

    def formfield_for_foreignkey(self, *args, **kwargs):
        return self.build__formfield_for_foreignkey(TagAdmin)(self, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return self.build__get_queryset(TagAdmin)(self, *args, **kwargs)


class TypeAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = (
        'user',
        'name',
    )
    list_filter = (
        # 'user',
    )

    def formfield_for_foreignkey(self, *args, **kwargs):
        return self.build__formfield_for_foreignkey(TypeAdmin)(self, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return self.build__get_queryset(TypeAdmin)(self, *args, **kwargs)


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


class TxAdmin(BaseAdmin, admin.ModelAdmin):
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
        # 'user',
        # 'account',
        # 'account__currency',
        'created_at',
        # 'type',
    )

    def formfield_for_foreignkey(self, *args, **kwargs):
        return self.build__formfield_for_foreignkey(TxAdmin)(self, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return self.build__get_queryset(TxAdmin)(self, *args, **kwargs)

# admin.site.register(Tag, TagAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Tx, TxAdmin)
admin.site.register(Account, AccountAdmin)
