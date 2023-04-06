# Generated by Django 3.2 on 2023-04-06 18:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]