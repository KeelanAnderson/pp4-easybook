from django.contrib import admin
from .models import Post, Service
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    search_fields = ['business_owner', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('business_owner',)}
    summernote_fields = ('content')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'business_owner', 'price']

