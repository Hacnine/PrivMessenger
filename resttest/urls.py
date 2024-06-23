from django.urls import path
from . import views

urlpatterns = [
    # path("", views.course_info, name="course_index"),
    path('create/', views.create_course, name='create_course'),
    path('info/', views.course_info, name="list_courses"),
    path('info/<int:pk>/', views.course_info, name="get_course"),
    path('update/<int:pk>/', views.update_course, name="update_course"),
    path('delete/<int:pk>/', views.delete_course, name="delete_course"),
    # path('delete/<int:id>/', views.delete_course, name='delete')

]
