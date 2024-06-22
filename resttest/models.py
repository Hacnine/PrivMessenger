from django.db import models


class Course(models.Model):
    DoesNotExist = None
    teacher_name = models.CharField(max_length=50)
    student_name = models.CharField(max_length=50)
    course_duration = models.IntegerField()
    seat = models.IntegerField()

    def __str__(self):
        return f'Course: {self.teacher_name} {self.student_name} {self.seat}'
