from django.contrib import admin
from .models import *


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'img', 'file']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['user', 'group_name', 'group_img']
