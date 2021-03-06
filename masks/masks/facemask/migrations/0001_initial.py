# Generated by Django 3.2.9 on 2021-11-08 14:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandMasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('enlace', models.CharField(max_length=300)),
                ('photo', models.CharField(max_length=300)),
                ('category', models.CharField(choices=[('Infantil', 'Infantil'), ('Deportes', 'Deportes'), ('Casual', 'Casual'), ('Raro', 'Raro')], max_length=15)),
                ('price', models.FloatField(default=5.0, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(5.0)])),
            ],
        ),
    ]
