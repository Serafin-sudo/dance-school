from django.http import HttpResponse
from django.shortcuts import render
from school.models import Classroom
from school.models import Course
from school.models import DayOfTheWeek

__all__ = [
    "home",
    "about"
]

def test_view(request):
    return HttpResponse("View di prova con HttpResponse")

def home(request):
    return render(
        request,
        template_name="home.html",
    )

def about(request):
    return render(
        request,
        template_name="about.html",
    )

def lista_aule(request):
    aule = Classroom.objects.all()
    return render(request, "aule.html", {"aule": aule})

def lista_giorni(request):
    giorni = DayOfTheWeek.objects.all()
    return render(request, "giorni.html", {"giorni": giorni})

def lista_corsi(request):
    corsi = Course.objects.all()
    return render(request, "corsi.html", {"corsi": corsi})