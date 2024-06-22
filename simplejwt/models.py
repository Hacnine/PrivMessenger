from django.db import models
from .managers import CustomManager


class CommonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    fees = models.IntegerField()
    data = None

    # students = models.Manager()
    students = CustomManager()


class Teacher(CommonInfo):
    salary = models.IntegerField()


class Constractor(CommonInfo):
    data = models.DateTimeField()
    salary = models.IntegerField()
