# Generated by Django 3.2 on 2023-04-16 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_remove_product_photo4'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Items',
        ),
    ]