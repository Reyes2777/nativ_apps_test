from django.urls import path

from course_manager.views import home, create_course, delete_course, update_course, create_student, students, \
    delete_student, update_student

urlpatterns = [
    path('', home, name='home'),
    path('create-course', create_course, name='create_course'),
    path('delete/<int:pk>/', delete_course, name='delete_course'),
    path('update/<int:pk>/', update_course, name='update_course'),
    path('students', students, name='students'),
    path('create-student', create_student, name='create_student'),
    path('delete-student/<int:pk>/', delete_student, name='delete_student'),
    path('update-student/<int:pk>/', update_student, name='update_student')
]
