# Generated by Django 3.2.7 on 2021-10-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_useraccounts_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccounts',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
