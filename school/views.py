from django.shortcuts import render, get_object_or_404
from schoolmanagement.models import School
from school.models import Course

def scuola(request, pk):
    scuola = get_object_or_404(School, pk=pk)
    corsi = Course.objects.filter(school=scuola).select_related(
        'classroom', 'day_of_the_week', 'school'
    )
    return render(request, "school/school_detail.html", {
        'object': scuola,
        'corsi': corsi,
    })