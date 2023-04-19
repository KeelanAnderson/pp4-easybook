from django import forms
from django.utils.text import slugify
from django.urls import reverse
from django.forms import ModelForm
from .models import Post, Service
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button


class CreatePostForm(forms.ModelForm):

    title = forms.CharField(max_length=80, required=True)
    slug = forms.CharField(max_length=80, required=True)

    def __init__(self, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Create', css_class='my-3 btn-primary'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='my-3 btn-secondary',
                             onclick="window.location.href = '{}';".format(reverse('manage_post'))))
        self.helper.form_method = 'POST'

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


class CreateServiceForm(forms.ModelForm):

    title = forms.ModelChoiceField(queryset=Post.objects.all())

    def __init__(self, *args, **kwargs):
        super(CreateServiceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Create', css_class='my-3 btn-primary'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='my-3 btn-secondary',
                             onclick="window.location.href = '{}';".format(reverse('manage_post'))))
        self.helper.form_method = 'POST'

    class Meta:
        model = Service
        fields = ['service_name', 'title', 'price']


class UpdateServiceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UpdateServiceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Update', css_class='my-3 btn-primary'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='my-3 btn-secondary',
                             onclick="window.location.href = '{}';".format(reverse('manage_post'))))
        self.helper.form_method = 'POST'

    class Meta:
        model = Service
        fields = ['service_name', 'price']

