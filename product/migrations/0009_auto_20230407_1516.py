# Generated by Django 3.2 on 2023-04-07 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20230407_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_details',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product_details',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='product_details',
            name='product_photo4',
        ),
    ]
