# Generated by Django 4.2.3 on 2023-07-12 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configs_settings', '0017_alter_worklocation_branch_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storage_category', models.CharField(blank=True, choices=[('WareHouse', 'Warehouse'), ('Distribution Point', 'Distribution Point')], default='', max_length=500, null=True, verbose_name='Storage Type')),
                ('storage_name', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Storage Name')),
                ('storage_code', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Storage Code')),
                ('capacity', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Storage Capacity(Sq M)')),
                ('address', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Address')),
                ('storage_manager', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Storage Manager')),
                ('latitude', models.FloatField(blank=True, default=0, null=True, verbose_name='Latitude')),
                ('longitude', models.FloatField(blank=True, default=0, null=True, verbose_name='Longitude')),
                ('start_date', models.DateField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configs_settings.cities')),
            ],
            options={
                'verbose_name': 'Storage',
                'verbose_name_plural': 'Storages',
            },
        ),
    ]
