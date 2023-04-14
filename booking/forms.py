from django import forms
from django.utils.text import slugify
from django.forms import ModelForm
from .models import Post


class CreatePostForm(forms.ModelForm):

    title = forms.CharField(max_length=80, required=True)
    slug = forms.CharField(max_length=80, required=True)

    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
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

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     slug = slugify(title)
    #     if Post.objects.filter(slug=slug).exists():
    #         raise forms.ValidationError('A post with this title already exists.')
    #     return slug
