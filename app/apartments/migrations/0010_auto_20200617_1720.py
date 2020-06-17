# Generated by Django 3.0.6 on 2020-06-17 14:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apartments', '0009_auto_20200615_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartments',
            name='is_favorite',
        ),
        migrations.AddField(
            model_name='apartments',
            name='is_favorite',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
