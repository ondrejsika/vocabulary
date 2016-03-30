from django.contrib import admin

from vocabulary.models import Course, Topic, Vocabulary


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


class CourseAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = (
        'user',
        'name',
    )
    list_filter = (
        # 'user',
    )

    def formfield_for_foreignkey(self, *args, **kwargs):
        return self.build__formfield_for_foreignkey(CourseAdmin)(self, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return self.build__get_queryset(CourseAdmin)(self, *args, **kwargs)


class TopicAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = (
        'user',
        'course',
        'name',
    )
    list_filter = (
        # 'user',
    )

    def formfield_for_foreignkey(self, *args, **kwargs):
        return self.build__formfield_for_foreignkey(TopicAdmin)(self, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return self.build__get_queryset(TopicAdmin)(self, *args, **kwargs)


class VocabularyAdmin(BaseAdmin, admin.ModelAdmin):
    list_display = (
        'user',
        'topic',
        'source',
        'target',
    )
    list_filter = (
        # 'user',
    )

    def formfield_for_foreignkey(self, *args, **kwargs):
        return self.build__formfield_for_foreignkey(VocabularyAdmin)(self, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return self.build__get_queryset(VocabularyAdmin)(self, *args, **kwargs)


admin.site.register(Course, CourseAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Vocabulary, VocabularyAdmin)

