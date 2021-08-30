import time
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ugettext
from solo.models import SingletonModel
from os.path import splitext


def profile_picture_directory_path(instance, filename):
    name, extension = splitext(filename)
    return 'header/profile_picture/{0}/{1}_{2}{3}'.format(
        name, str(int(time.time())), str(uuid.uuid4())[:8], extension
    )


def image_directory_path(instance, filename):
    name, extension = splitext(filename)
    return 'header/{0}/{1}_{2}{3}'.format(
        name, str(int(time.time())), str(uuid.uuid4())[:8], extension
    )


class GeneralSettings(SingletonModel):
    header_background_color = models.CharField(max_length=255)
    header_background_image = models.ImageField(
        upload_to=image_directory_path,
        max_length=255,
        blank=True,
        null=True
    )
    header_profile_picture = models.ImageField(
        upload_to=image_directory_path,
        max_length=255
    )

    def __str__(self):
        return ugettext('General settings')

    class Meta:
        verbose_name = _('general settings')


class Contact(models.Model):
    settings = models.OneToOneField(
        GeneralSettings,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    address = models.CharField(_('Address'), max_length=255)
    phone = models.CharField(_('Phone'), max_length=16)
    instagram_url = models.URLField()
    facebook_url = models.URLField()
    booking_url = models.URLField()

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')


class Content(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    navbar_title = models.CharField(_('Navbar title'), max_length=255, blank=True, null=True)
    text = models.TextField(_('Text'))
    order = models.PositiveIntegerField(_('Order'), default=0)
    collapse_long_text = models.BooleanField(default=False)

    class Meta:
        ordering = ('order',)


class Category(models.Model):
    title = models.CharField(_('Name'), max_length=255)
    tooltip = models.TextField(_('Tooltip'), blank=True, null=True)
    order = models.PositiveIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('order',)


class Service(models.Model):
    category = models.ForeignKey(
        Category,
        null=True,
        related_name='services',
        on_delete=models.SET_NULL
    )
    name = models.CharField('Nimi', max_length=255)
    length = models.IntegerField('Kesto')
    price = models.DecimalField(
        _('Price (€)'), max_digits=5, decimal_places=2
    )
    order = models.PositiveIntegerField(_('Order'), default=0)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
        ordering = ('order',)
