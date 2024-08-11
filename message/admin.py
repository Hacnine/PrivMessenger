from django.contrib import admin
from .models import *


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'file', 'created_at', 'updated_at']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['message', 'img']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['user', 'group_name', 'group_img']
