# Generated by Django 3.2 on 2023-04-16 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_rename_product_items'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Product',
        ),
    ]
