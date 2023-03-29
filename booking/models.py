from django.core.validators import RegexValidator, validate_email
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from location_field.models.plain import PlainLocationField


STATUS = ((0, 'draft'), (1, 'public'))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    profession = models.CharField(max_length=200, default='n/a')
    city = models.CharField(max_length=255, default='n/a')
    location = PlainLocationField(based_fields=['city'], zoom=7, default='n/a')
    content = models.TextField(default='')
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False, default='n/a')
    email = models.EmailField(validators=[validate_email], blank=False, default='n/a')
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
