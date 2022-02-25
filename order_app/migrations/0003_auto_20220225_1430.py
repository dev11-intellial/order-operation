# Generated by Django 3.2.12 on 2022-02-25 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0002_auto_20220225_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='qty',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
