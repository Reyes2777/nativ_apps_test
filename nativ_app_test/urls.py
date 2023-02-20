"""nativ_app_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from course_manager.views import CourseList, CourseCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', TemplateView.as_view(template_name='main.html'), name='main'),
    path('courses/', CourseList.as_view(template_name='courses/index.html'), name='courses_list'),
    path('courses/create', CourseCreate.as_view(template_name='courses/create.html'), name='courses_create'),

]
