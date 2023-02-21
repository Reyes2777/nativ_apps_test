from django import forms
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from course_manager.forms import CourseForm
from course_manager.models import Course


def home(_request):
    form = CourseForm
    courses = Course.objects.all()
    context = {'form': form, 'courses': courses}
    return render(_request, 'courses/index.html', context)


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            data = {
                'name': course.name,
                'schedule': course.schedule,
                'start_date': course.start_date,
                'end_date': course.end_date,
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Formulario inválido.'}, status=400)
    else:
        return JsonResponse({'error': 'Método HTTP no permitido.'}, status=405)


@ensure_csrf_cookie
@require_POST
def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST, instance=course)
    if form.is_valid():
        form.save()
        data = {'success': True}
    else:
        data = {'success': False, 'errors': form.errors}
    return JsonResponse(data)


@ensure_csrf_cookie
@require_POST
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    data = {'success': True}
    return JsonResponse(data)


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
    fields = ('name', 'schedule', 'start_date', 'end_date')
    success_message = 'Curso actualizado exitosamente !'

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


class CourseDelete(SuccessMessageMixin, DeleteView):
    model = Course
    form = Course
    fields = '__all__'

    def get_success_url(self):
        success_message = 'Curso eliminado exitosamente'
        messages.success(self.request, success_message)
        return reverse('courses_list')
