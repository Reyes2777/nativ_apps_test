from django import forms
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
    fields = ('name', 'schedule', 'start_date', 'end_date')
    success_message = 'Curso creado exitosamente'

    def get_success_url(self):
        return reverse('courses_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['start_date'].widget = forms.DateInput(attrs={'type': 'date'})
        form.fields['end_date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']

        if start_date > end_date:
            form.add_error('start_date', 'La fecha de inicio no puede ser mayor que la fecha de finalización')
            return super().form_invalid(form)

        return super().form_valid(form)


class CourseDetail(DetailView):
    model = Course


class CourseUpdate(SuccessMessageMixin, UpdateView):
    model = Course
    form = Course
    fields = 'all_fields'
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
