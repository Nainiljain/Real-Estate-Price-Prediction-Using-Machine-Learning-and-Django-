# Generated by Django 5.0.3 on 2024-03-23 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappfinal', '0009_alter_property_propertyfromdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='PropertyFromDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 23, 16, 41, 25, 175343)),
        ),
        migrations.AlterField(
            model_name='property',
            name='PropertyToDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 23, 16, 41, 25, 175343)),
        ),
    ]
