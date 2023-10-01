# Generated by Django 3.2 on 2023-04-07 15:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20230407_1516'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_details',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(default='SOME STRING'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]