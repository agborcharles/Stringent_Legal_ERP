# Generated by Django 4.2.3 on 2023-07-30 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0010_alter_salesinvoices_status'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SalesInvoices',
            new_name='Payment',
        ),
    ]