from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    schedule = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    courses = models.ManyToManyField('Course', related_name='enrolled_students', blank=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'
