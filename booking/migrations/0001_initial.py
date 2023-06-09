# Generated by Django 3.2.18 on 2023-04-12 14:18

import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, unique=True)),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('profession', models.CharField(default='n/a', max_length=80)),
                ('about', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='n/a', max_length=255)),
                ('location', location_field.models.plain.PlainLocationField(default='n/a', max_length=63)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('carousel_images', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='images')),
                ('phone_number', models.CharField(default='n/a', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(default='n/a', max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'public')], default=0)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=80)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='booking.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='display_services',
            field=models.ManyToManyField(blank=True, to='booking.Service'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.CharField(choices=[('A', '9:00-10:00'), ('B', '10:00-11:00'), ('C', '11:00-12:00'), ('D', '12:00-13:00'), ('E', '13:00-14:00'), ('F', '14:00-15:00'), ('G', '15:00-16:00'), ('H', '16:00-17:00')], default='A', max_length=2)),
                ('booking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.service')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
