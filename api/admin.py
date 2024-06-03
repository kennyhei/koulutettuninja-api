from datetime import timedelta
from django.contrib import admin
from django.utils import timezone
from django_q.models import Schedule
from django_q.tasks import schedule
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableTabularInline
from solo.admin import SingletonModelAdmin
from api import models


class ModelUpdateDeployMixin:

    def _schedule_deploy(self):
        if Schedule.objects.exists():
            return
        schedule(
            'api.tasks.task_deploy_front',
            name='front_deploy',
            schedule_type=Schedule.ONCE,
            next_run=timezone.now() + timedelta(minutes=10)
        )

    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        self._schedule_deploy()

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        self._schedule_deploy()


@admin.register(models.GeneralSettings)
class GeneralSettingsAdmin(ModelUpdateDeployMixin, SingletonModelAdmin):

    class ContactInline(admin.StackedInline):
        model = models.Contact

    inlines = (
        ContactInline,
    )


@admin.register(models.Notification)
class NotificationAdmin(ModelUpdateDeployMixin, SingletonModelAdmin):
    list_display = (
        '_text',
        'show_notification',
    )

    def _text(self, obj):
        text = obj.text
        if not text:
            return None
        return text[:220] + '...'


@admin.register(models.Content)
class ContentAdmin(ModelUpdateDeployMixin, SortableAdminMixin, admin.ModelAdmin):
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
class CategoryAdmin(ModelUpdateDeployMixin, SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        'title',
        'deleted_at',
    )

    class ServiceInline(SortableTabularInline):
        model = models.Service

    inlines = (
        ServiceInline,
    )


@admin.register(models.Service)
class ServiceAdmin(ModelUpdateDeployMixin, admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'length',
        'price',
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category')
