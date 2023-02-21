from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', TemplateView.as_view(template_name='main.html'), name='main'),
    path('courses/', include('course_manager.urls'))
    ]
