# Generated by Django 3.0.6 on 2020-06-15 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0008_apartments_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
