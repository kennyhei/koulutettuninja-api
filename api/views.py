from rest_framework import viewsets
from api import models
from api import serializers


class GeneralSettingsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GeneralSettingsSerializer
    queryset = models.GeneralSettings.objects.all()


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContactSerializer
    queryset = models.Contact.objects.all()


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NotificationSerializer
    queryset = models.Notification.objects.all()


class ContentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContentSerializer
    queryset = models.Content.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.filter(deleted_at__isnull=True).all()


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ServiceSerializer
    queryset = models.Service.objects.all()
