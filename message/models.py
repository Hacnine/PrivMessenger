from django.db import models
from django.conf import settings
from account.models import User


class ChatRoom(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    participants = models.ManyToManyField(User, related_name='chatrooms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.participants.count() == 2:
            return f"Chatroom between {self.participants.all()[0].name} and {self.participants.all()[1].name}"
        return self.name or "Group Chat"

    def get_chatroom_name_for_user(self, user):
        other_participant = self.participants.exclude(id=user.id).first()
        return other_participant.name if other_participant else self.name


class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    url = models.URLField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender.email} to {self.chatroom}: {self.message}"


class Image(models.Model):
    message = models.ForeignKey(Message, related_name='images', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/chat_images/', null=True, blank=True)

    def __str__(self):
        return f"Image for message {self.message.id}"


class File(models.Model):
    message = models.ForeignKey(Message, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='static/chat_files/', null=True, blank=True)

    def __str__(self):
        return f"File for message {self.message.id}"
