# Generated by Django 3.0.6 on 2020-06-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0007_auto_20200608_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartments',
            name='is_favorite',
            field=models.BooleanField(default=True),
        ),
    ]
