from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    schedule = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def number_students(self):
        return len(self.enrolled_students.all())


class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    courses = models.ManyToManyField('Course', related_name='enrolled_students', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'
