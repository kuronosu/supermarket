# Generated by Django 3.2.8 on 2021-10-17 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_name'),
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
