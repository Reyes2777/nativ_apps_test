from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

from course_manager.forms import CourseForm, StudentForm
from course_manager.models import Course, Student


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


def students(_request):
    form = StudentForm
    students = Student.objects.all()
    context = {'form': form, 'students': students}
    return render(_request, 'students/index.html', context)


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            data = {
                'name': student.name,
                'last_name': student.last_name,
                'age': student.age,
                'email': student.email,
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Formulario inválido.'}, status=400)
    else:
        return JsonResponse({'error': 'Método HTTP no permitido.'}, status=405)


@ensure_csrf_cookie
@require_POST
def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        data = {'success': True}
    else:
        data = {'success': False, 'errors': form.errors}
    return JsonResponse(data)


@ensure_csrf_cookie
@require_POST
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    data = {'success': True}
    return JsonResponse(data)


def list_students(request, course_id):
    course = Course.objects.get(id=course_id)
    students = course.enrolled_students.all()
    data = {
        'students': [{
            'id': s.id,
            'name': s.name + ' ' + s.last_name,
            'email': s.email,
        } for s in students]
    }
    return JsonResponse(data)
