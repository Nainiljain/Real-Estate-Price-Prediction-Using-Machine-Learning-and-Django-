# Generated by Django 5.0.3 on 2024-03-21 11:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappfinal', '0007_property_category_alter_property_propertyfromdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='PropertyFromDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 21, 17, 5, 48, 704444)),
        ),
        migrations.AlterField(
            model_name='property',
            name='PropertyToDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 21, 17, 5, 48, 704444)),
        ),
    ]
