# Generated by Django 3.2.6 on 2021-08-30 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generalsettings',
            old_name='header_background',
            new_name='header_background_color',
        ),
    ]
