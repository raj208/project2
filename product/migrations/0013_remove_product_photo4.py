# Generated by Django 3.2 on 2023-04-16 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_product_photo4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photo4',
        ),
    ]
