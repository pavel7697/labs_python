from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import teacher
from .models import pulpit
from grow.connection import Connection, pulpit
# Create your views here..


def index(request):
    # conn = Connection("dbuser", "123", "first_db")
    # with conn:
    #     ded = pulpit(conn, 'rt3', 1798)
    #     # ded.save()
    #     teachers = ded.show()
    teachers = teacher.objects.all()
    content = {
        'teachers': teachers
    }
    for a in teachers:
        print(a)
    return render(request, 'teachers.html', content)


def Pit(request):
    pul = pulpit.objects.all()
    content = {
        'pulpits': pul
    }
    return render(request, 'single.html', content)
    pass