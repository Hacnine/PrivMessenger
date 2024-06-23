from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseModel(admin.ModelAdmin):
    list_display = ["teacher_name", "student_name", "course_duration", "seat"]
