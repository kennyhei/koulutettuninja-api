# Generated by Django 4.1.6 on 2024-06-03 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_category_deleted_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('show_notification', models.BooleanField(default=False, verbose_name='Show notification')),
            ],
        ),
    ]
