from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from course_manager.models import Course


class CourseList(ListView):
    model = Course


class CourseCreate(SuccessMessageMixin, CreateView):
    model = Course
    form = Course
    fields = 'all'
    success_message = 'Curso creado exitosamente'

    def get_success_url(self):
        return reverse('courses_list')


class CourseDetail(DetailView):
    model = Course


class CourseUpdate(SuccessMessageMixin, UpdateView):
    model = Course
    form = Course
    fields = '__all__'
    success_message = 'Curso actualizado exitosamente !'

    def get_success_url(self):
        return reverse('courses_list')


class CourseDelete(SuccessMessageMixin, DeleteView):
    model = Course
    form = Course
    fields = '__all__'

    def get_success_url(self):
        success_message = 'Curso eliminado exitosamente'
        messages.success(self.request, success_message)
        return reverse('courses_list')
