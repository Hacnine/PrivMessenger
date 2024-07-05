from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        

class Message(models.Model):
    DoesNotExist = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=2000, null=True, blank=True)
    img = models.ImageField(upload_to='chat_images/', null=True, blank=True)
    file = models.FileField(upload_to='chat_files/', null=True, blank=True)


class Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, limit_choices_to={'is_staff': True})
    group_name = models.CharField(max_length=150, )
    group_img = models.ImageField(upload_to='group_profile_images/')
