from django.urls import path

from course_manager.views import CourseList, CourseCreate, CourseUpdate, CourseDelete, CourseDetail


urlpatterns = [
    path('', CourseList.as_view(template_name='courses/index.html'), name='courses_list'),
    path('create', CourseCreate.as_view(template_name='courses/create.html'), name='courses_create'),
    path('<int:pk>/detail/', CourseDetail.as_view(template_name='courses/detail.html'), name='course_detail'),
    path('<int:pk>/update/', CourseUpdate.as_view(template_name='courses/update.html'), name='course_update'),
    path('<int:pk>/delete/', CourseDelete.as_view(template_name='courses/delete.html'), name='course_delete'),
]
