# Generated by Django 3.2 on 2023-10-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_remove_team_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
