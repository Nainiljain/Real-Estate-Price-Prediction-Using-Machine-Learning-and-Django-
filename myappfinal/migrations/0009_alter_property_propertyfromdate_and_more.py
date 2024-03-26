import datetime
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [

        ('myappfinal', '0008_merge_20240326_0538'),

        ('myappfinal', '0008_merge_20240323_1634'),

    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='PropertyFromDate',

            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 26, 5, 56, 48, 7257)),

            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 23, 16, 39, 32, 55246)),

        ),
        migrations.AlterField(
            model_name='property',
            name='PropertyToDate',

            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 26, 5, 56, 48, 7291)),

            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 23, 16, 39, 32, 55246)),

        ),
    ]
