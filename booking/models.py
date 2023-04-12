from django.core.validators import RegexValidator, validate_email
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from location_field.models.plain import PlainLocationField
from datetime import datetime

STATUS = ((0, 'draft'), (1, 'public'))


class Post(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    profession = models.CharField(max_length=80, default='n/a')
    about = models.CharField(max_length=200, default='')
    display_services = models.ManyToManyField('Service', blank=True)
    city = models.CharField(max_length=255, default='n/a')
    location = PlainLocationField(based_fields=['city'], zoom=7, default='n/a')
    featured_image = CloudinaryField('image', default='placeholder')
    carousel_images = CloudinaryField('images', default='placeholder')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False, default='n/a')
    email = models.EmailField(validators=[validate_email], blank=False, default='n/a')
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Service(models.Model):
    service_name = models.CharField(max_length=80)
    title = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='services')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name


class Booking(models.Model):

    TIMESLOT_CHOICES = (
        ("A", "9:00-10:00"),
        ("B", "10:00-11:00"),
        ("C", "11:00-12:00"),
        ("D", "12:00-13:00"),
        ("E", "13:00-14:00"),
        ("F", "14:00-15:00"),
        ("G", "15:00-16:00"),
        ("H", "16:00-17:00"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    title = models.ForeignKey('Post', on_delete=models.CASCADE)
    booking_time = models.CharField(
        max_length=2,
        choices=TIMESLOT_CHOICES,
        default="A",
    )
    booking_date = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()

    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s Appointment for {self.service} with {self.title} on {self.booking_date} at {self.booking_time}"