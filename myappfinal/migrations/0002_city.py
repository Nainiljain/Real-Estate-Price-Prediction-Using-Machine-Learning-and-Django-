# Generated by Django 5.0.3 on 2024-03-18 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappfinal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CityName', models.CharField(max_length=30)),
                ('State', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myappfinal.state')),
            ],
        ),
    ]
