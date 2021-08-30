from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableInlineAdminMixin
from solo.admin import SingletonModelAdmin
from api import models


@admin.register(models.GeneralSettings)
class GeneralSettingsAdmin(SingletonModelAdmin):

    class ContactInline(admin.StackedInline):
        model = models.Contact

    inlines = (
        ContactInline,
    )


@admin.register(models.Content)
class ContentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        'order',
        'title',
        'navbar_title',
        '_text',
    )
    ordering = (
        'order',
    )

    def _text(self, obj):
        text = obj.text
        if not text:
            return None
        return text[:220] + '...'


@admin.register(models.Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        'title',
    )

    class ServiceInline(SortableInlineAdminMixin, admin.TabularInline):
        model = models.Service

    inlines = (
        ServiceInline,
    )


@admin.register(models.Service)
class ServiceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'length',
        'price',
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category')


'''
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'address',
        'phone',
        'instagram_url',
        'facebook_url',
        'booking_url',
    )
'''
