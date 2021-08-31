# Generated by Django 3.2.6 on 2021-08-31 08:07

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Name')),
                ('tooltip', models.TextField(blank=True, null=True, verbose_name='Tooltip')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('navbar_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Navbar title')),
                ('text', models.TextField(verbose_name='Text')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('collapse_long_text', models.BooleanField(default=False, verbose_name='Collapse long text')),
                ('show_pricing', models.BooleanField(default=False, verbose_name='Show pricing')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_background_color', models.CharField(max_length=255)),
                ('header_background_image', models.ImageField(blank=True, max_length=255, null=True, upload_to=api.models.image_directory_path)),
                ('header_profile_picture', models.ImageField(max_length=255, upload_to=api.models.image_directory_path)),
            ],
            options={
                'verbose_name': 'general settings',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nimi')),
                ('length', models.IntegerField(verbose_name='Kesto')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price (€)')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='api.category')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='Company name')),
                ('location_street_address', models.CharField(max_length=255, verbose_name='Steet address')),
                ('location_postcode', models.CharField(max_length=5, verbose_name='Postcode')),
                ('location_city', models.CharField(max_length=255, verbose_name='City')),
                ('phone', models.CharField(max_length=16, verbose_name='Phone')),
                ('instagram_url', models.URLField()),
                ('facebook_url', models.URLField()),
                ('booking_url', models.URLField()),
                ('settings', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.generalsettings')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
