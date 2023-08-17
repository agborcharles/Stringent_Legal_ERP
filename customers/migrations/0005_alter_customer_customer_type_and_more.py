# Generated by Django 4.2.3 on 2023-07-17 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_customer_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_type',
            field=models.CharField(blank=True, choices=[('Supermarket', 'Supermarket'), ('Wine Shop', 'Wine Shop'), ('Convenience Store', 'Convenience Store'), ('Restaurants', 'Restaurants'), ('Hotel', 'Hotel'), ('Snack Bar', 'Snack Bar'), ('Catering Service', 'Catering Service'), ('Individual', 'Individual'), ('Others', 'Others')], max_length=100, null=True, verbose_name='Customer Type'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='payment_terms',
            field=models.CharField(blank=True, choices=[('Immediate Payment', 'Immediate Payment'), ('15 Days', '15 Days'), ('30 Days', '30 Days'), ('45 Days', '45 Days'), ('2 Months', '2 Months'), ('End of Following Month', 'End of Following Month')], max_length=100, null=True, verbose_name='Payment Terms'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='quarter',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Quarter'),
        ),
    ]
