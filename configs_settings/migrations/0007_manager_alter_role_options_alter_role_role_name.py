# Generated by Django 4.2.3 on 2023-07-08 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configs_settings', '0006_alter_role_options_rename_name_role_role_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_name', models.CharField(max_length=100, verbose_name='Manager Name')),
                ('startdate', models.DateField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Manager',
                'verbose_name_plural': 'Managers',
                'ordering': ['manager_name'],
            },
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ['role_name'], 'verbose_name': 'Role', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(max_length=125, verbose_name='Role Name'),
        ),
    ]
