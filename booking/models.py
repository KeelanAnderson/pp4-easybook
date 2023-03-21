from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from location_field.models.plain import PlainLocationField


STATUS = ((0, 'draft'), (1, 'public'))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(default='')
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
