# Generated by Django 3.2.18 on 2023-04-19 09:37

import cloudinary.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20230414_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='carousel_images',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='Gallery Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='Main Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='phone_number',
            field=models.CharField(default='n/a', max_length=17, validators=[django.core.validators.RegexValidator(message="Must be in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'draft'), (1, 'public')], default=1),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
