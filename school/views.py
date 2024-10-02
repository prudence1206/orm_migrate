from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    object_list = Student.objects.all()
    print(object_list)
    students = Student.objects.all()
    for student in students:
        print(student.name)  # имя
        print(student.group)  # класс
    teachers = student.teachers.all()
    print(teachers)
    context = {'object_list':object_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
