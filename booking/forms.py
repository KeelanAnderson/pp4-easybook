from django import forms
from django.forms import ModelForm
from .models import Post


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'profession',
            'about',
            'city',
            'location',
            'featured_image',
            'carousel_images',
            'phone_number',
            'email',
            'status',
        ]
