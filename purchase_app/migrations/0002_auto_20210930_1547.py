# Generated by Django 3.2.7 on 2021-09-30 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_no',
            field=models.CharField(blank=True, editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_product_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
