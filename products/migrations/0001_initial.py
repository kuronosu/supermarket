# Generated by Django 3.2.8 on 2021-10-16 17:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='Price')),
            ],
        ),
    ]