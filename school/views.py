from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render

from school.models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    student_list = Student.objects.all().order_by(ordering)
    context = {'object_list': student_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = 'group'

    return render(request, template, context)

