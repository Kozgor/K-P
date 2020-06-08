# Generated by Django 3.0.6 on 2020-06-07 20:34

from django.db import migrations, models
import django.db.models.deletion

def string_to_id(apps, schema_editor):
    MyModel = apps.get_model('apartments', 'Apartments')
    for a in MyModel.objects.all():
        a.apartment_type = None
        a.save()

class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0004_auto_20200603_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='назва')),
            ],
        ),
        migrations.AlterField(
            model_name='apartments',
            name='apartment_type',
            field=models.CharField(null=True, max_length=100)
        ),
        migrations.RunPython(string_to_id),
    ]