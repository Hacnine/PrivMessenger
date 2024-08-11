from django.db import models
from django.conf import settings
from account.models import User


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=2000, null=True, blank=True)
    file = models.FileField(upload_to='static/chat_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.user.email}"


class Image(models.Model):
    message = models.ForeignKey(Message, related_name='images', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/chat_images/',  null=True, blank=True)

    def __str__(self):
        return f"Image for message {self.message.id}"


class Group(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, limit_choices_to={'is_staff': True})
    group_name = models.CharField(max_length=150, )
    group_img = models.ImageField(upload_to='group_profile_images/')

    def __str__(self):
        return self.group_name
