# Generated by Django 4.2.3 on 2023-07-09 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configs_settings', '0008_jobposition_remove_role_sub_department'),
        ('human_resource', '0009_remove_employee_firstname_remove_employee_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configs_settings.jobposition', verbose_name='Role'),
        ),
    ]