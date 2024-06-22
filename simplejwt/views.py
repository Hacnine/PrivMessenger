from django.shortcuts import render
from .models import Student


def home(request):
    student_data = Student.students.all()
    return render(request, 'school/home.ht  ml')
# Create your views here.
