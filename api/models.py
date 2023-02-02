import os
import sys
import time
import uuid

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils.translation import gettext_lazy as _
from io import BytesIO
from solo.models import SingletonModel
from os.path import splitext

from PIL import Image


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
        return str(_('General settings'))

    class Meta:
        verbose_name = _('general settings')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Resize uploaded profile picture
        if self.header_profile_picture:
            if os.path.exists(self.header_profile_picture.path):
                image = Image.open(self.header_profile_picture)
                output_io_stream = BytesIO()
                base_height = 220
                hpercent = base_height / image.size[1]
                wsize = int(image.size[0] * hpercent)
                image_temporary_resized = image.resize((wsize, base_height))
                image_temporary_resized.save(output_io_stream, format='JPEG')
                output_io_stream.seek(0)
                self.header_profile_picture = InMemoryUploadedFile(
                    output_io_stream,
                    'ImageField',
                    '{}.jpeg'.format(self.header_profile_picture.name.split('.')[0]),
                    'image/jpeg',
                    sys.getsizeof(output_io_stream), None
                )
        super().save(*args, **kwargs)


class Contact(models.Model):
    settings = models.OneToOneField(
        GeneralSettings,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    company_name = models.CharField(_('Company name'), blank=True, max_length=255)
    location_street_address = models.CharField(_('Steet address'), blank=True, max_length=255)
    location_postcode = models.CharField(_('Postcode'), blank=True, max_length=5)
    location_city = models.CharField(_('City'), max_length=255)
    phone = models.CharField(_('Phone'), max_length=16, blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    google_maps_url = models.URLField(max_length=500, blank=True, null=True)
    booking_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')


class Content(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    navbar_title = models.CharField(_('Navbar title'), max_length=255, blank=True, null=True)
    text = models.TextField(_('Text'))
    order = models.PositiveIntegerField(_('Order'), default=0)
    collapse_long_text = models.BooleanField(_('Collapse long text'), default=False)
    # Hacky but will do and is easier for end-user to toggle
    # rather than set foreign key to Content in Category model
    show_pricing = models.BooleanField(_('Show pricing'), default=False)
    show_booking_btn = models.BooleanField(_('Show booking button'), default=False)
    show_in_navbar = models.BooleanField(_('Show in navbar'), default=True)
    hide_content = models.BooleanField(_('Hide content'), default=False)

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
