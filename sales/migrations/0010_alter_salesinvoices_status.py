# Generated by Django 4.2.3 on 2023-07-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_salesinvoices_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesinvoices',
            name='status',
            field=models.CharField(blank=True, choices=[('Sales', 'Sales'), ('Returns', 'Returns')], default='Sales', help_text='Sales / Returns', max_length=500, null=True, verbose_name='Transaction Status'),
        ),
    ]
