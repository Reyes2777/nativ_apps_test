# Generated by Django 4.1.7 on 2023-02-22 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='enrolled_students', to='course_manager.course'),
        ),
    ]
