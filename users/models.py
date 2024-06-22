from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.contrib.auth.models import User


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    passmessage = models.CharField(max_length=255,  default='shuvo sokal')
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'User: {self.username} {self.passmessage}'


# class Page(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     # user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
#
#     page_name = models.CharField(max_length=70)
#     page_cat = models.CharField(max_length=70)
#     page_publish_data = models.DateField()


