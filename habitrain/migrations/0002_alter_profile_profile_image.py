# Generated by Django 3.2.20 on 2023-07-10 20:37

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habitrain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='avatar.jpg', max_length=255, verbose_name='image'),
        ),
    ]
