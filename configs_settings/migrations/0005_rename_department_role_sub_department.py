# Generated by Django 4.2.3 on 2023-07-08 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configs_settings', '0004_role_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='department',
            new_name='sub_department',
        ),
    ]