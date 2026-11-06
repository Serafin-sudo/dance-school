from django.shortcuts import render, get_object_or_404
from schoolmanagement.models import School
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy
from school.models import Course, Classroom, DayOfTheWeek

def scuola(request, pk):
    scuola = get_object_or_404(School, pk=pk)
    corsi = Course.objects.filter(school=scuola).select_related(
        'classroom', 'day_of_the_week', 'school'
    )
    return render(request, "school/school_detail.html", {
        'object': scuola,
        'corsi': corsi,
    })

# corso
class CourseCreateView(CreateView):
    model = Course
    fields = ["subject", "day_of_the_week", "starting_hour", "classroom", "school"]
    template_name = "school/form_course.html"
    success_url = reverse_lazy("corsi")

class CourseUpdateView(UpdateView):
    model = Course
    fields = ["subject", "starting_hour", "classroom", "school", "day_of_the_week"]
    template_name = "school/form_course.html"
    success_url = reverse_lazy("corsi")

# aula
class ClassroomCreateView(CreateView):
    model = Classroom
    fields = ["name", "capacity"]
    template_name = "school/form_classroom.html"
    success_url = reverse_lazy("aule")

class ClassroomUpdateView(UpdateView):
    model = Classroom
    fields = ["name", "capacity"]
    template_name = "school/form_classroom.html"
    success_url = reverse_lazy("aule")


# giorno della settimana
class DayCreateView(CreateView):
    model = DayOfTheWeek
    fields = ["number", "name"]
    template_name = "school/form_day.html"
    success_url = reverse_lazy("giorni")

class DayUpdateView(UpdateView):
    model = DayOfTheWeek
    fields = ["number", "name"]
    template_name = "school/form_day.html"
    success_url = reverse_lazy("giorni")