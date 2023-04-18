from django import forms
from django.utils.text import slugify
from django.forms import ModelForm
from .models import Post, Service
import cloudinary


class CreatePostForm(forms.ModelForm):

    title = forms.CharField(max_length=80, required=True)
    slug = forms.CharField(max_length=80, required=True)
    featured_image = cloudinary.forms.CloudinaryFileField()
    carousel_images = cloudinary.forms.CloudinaryFileField()

    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'profession',
            'about',
            'display_services',
            'city',
            'location',
            'featured_image',
            'carousel_images',
            'phone_number',
            'email',
            'status',
        ]


class CreateServiceForm(forms.ModelForm):

    title = forms.ModelChoiceField(queryset=Post.objects.all())

    class Meta:
        model = Service
        fields = ['service_name', 'title', 'price']


class UpdateServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['service_name', 'price']

