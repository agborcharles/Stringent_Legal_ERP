# Generated by Django 4.2.3 on 2023-07-12 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0009_remove_storage_city'),
        ('storage_location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='storage_location',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='storage_location.storage', verbose_name='Product Category'),
        ),
        migrations.DeleteModel(
            name='Storage',
        ),
    ]
