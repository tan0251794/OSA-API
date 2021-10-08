# Generated by Django 3.2.7 on 2021-10-04 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_app', '0004_auto_20211003_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 4, 19, 1, 32, 137417)),
        ),
        migrations.AlterField(
            model_name='pack',
            name='arrived_date',
            field=models.TimeField(default=datetime.datetime(2021, 10, 4, 19, 1, 32, 140414)),
        ),
        migrations.AlterField(
            model_name='pack',
            name='to_start_ship_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 4, 19, 1, 32, 140414)),
        ),
    ]