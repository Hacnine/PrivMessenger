from django.contrib import admin
from .models import ChatRoom, Message, Image, File


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    filter_horizontal = ['participants']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['chatroom', 'sender', 'message', 'created_at', 'updated_at']
    search_fields = ['chatroom__name', 'sender__email', 'message']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['message', 'img']


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['message', 'file']
