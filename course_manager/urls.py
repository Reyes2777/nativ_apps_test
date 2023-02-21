from django.urls import path

from course_manager.views import home, create_course, delete_course, update_course

urlpatterns = [
    path('', home, name='home'),
    path('create-course', create_course, name='create_course'),
    path('delete/<int:pk>/', delete_course, name='delete_course'),
    path('update/<int:pk>/', update_course, name='update_course'),
    # path('create', CourseCreate.as_view(template_name='courses/create.html'), name='courses_create'),
    # path('<int:pk>/detail/', CourseDetail.as_view(template_name='courses/detail.html'), name='course_detail'),
    # path('<int:pk>/update/', CourseUpdate.as_view(template_name='courses/update.html'), name='course_update'),
    # path('<int:pk>/delete/', CourseDelete.as_view(template_name='courses/delete.html'), name='course_delete'),
]
