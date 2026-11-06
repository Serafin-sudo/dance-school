from django.shortcuts import render, get_object_or_404
from schoolmanagement.models import School
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from school.models import Course
from school.models import Classroom
from school.models import DayOfTheWeek

def scuola(request, pk):
    scuola = get_object_or_404(School, pk=pk)
    corsi = Course.objects.filter(school=scuola).select_related(
        'classroom', 'day_of_the_week', 'school'
    )
    return render(request, "school/school_detail.html", {
        'object': scuola,
        'corsi': corsi,
    })

def modifica_corso(request, pk):
    corso = get_object_or_404(Course, pk=pk)
    return render(request, "school/form_course.html", {"corso": corso})

class CourseUpdateView(UpdateView):
    model = Course
    fields = ["subject", "starting_hour", "classroom", "school", "day_of_the_week"]
    template_name = "school/form_course.html"
    success_url = reverse_lazy("corsi")
    
def modifica_aula(request, pk):
    aula = get_object_or_404(Course, pk=pk)
    return render(request, "school/form_classroom.html", {"aula": aula})

class ClassroomUpdateView(UpdateView):
    model = Classroom
    fields = ["name", "capacity"]
    template_name = "school/form_classroom.html"
    success_url = reverse_lazy("aule")
    
def modifica_giorno(request, pk):
    giorno = get_object_or_404(Course, pk=pk)
    return render(request, "school/form_day.html", {"giorno": giorno})

class DayUpdateView(UpdateView):
    model = DayOfTheWeek
    fields = ["number", "name"]
    template_name = "school/form_day.html"
    success_url = reverse_lazy("giorni")