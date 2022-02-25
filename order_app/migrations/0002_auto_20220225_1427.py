# Generated by Django 3.2.12 on 2022-02-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contact_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
