# Generated by Django 4.2.3 on 2023-07-09 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0011_alter_employee_manager'),
        ('configs_settings', '0014_remove_manager_work_location_branchmanager_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Manager',
        ),
    ]