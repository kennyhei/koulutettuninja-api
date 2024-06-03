from rest_framework import serializers
from api import models


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contact
        exclude = ('id', 'settings',)


class GeneralSettingsSerializer(serializers.ModelSerializer):

    contact = ContactSerializer()

    class Meta:
        model = models.GeneralSettings
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Notification
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Content
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Service
        fields = (
            'order',
            'name',
            'length',
            'price',
        )


class CategorySerializer(serializers.ModelSerializer):

    services = ServiceSerializer(many=True)

    class Meta:
        model = models.Category
        fields = '__all__'
