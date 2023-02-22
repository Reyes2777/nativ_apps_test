from django import forms
from django.forms import TextInput, DateInput
from course_manager.models import Course, Student


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'schedule', 'start_date', 'end_date']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name_id'}),
            'schedule': TextInput(attrs={'class': 'form-control', 'id': 'schedule_id'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'id': 'start_date_id', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'id': 'end_date_id', 'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError('La fecha de inicio no puede ser mayor que la fecha de finalización')

        return cleaned_data


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'last_name', 'age', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
