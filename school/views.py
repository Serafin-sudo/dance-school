from django.shortcuts import render

def scuola(request, pk):
    scuola = get_object_or_404(School, pk=pk)
    corsi = Course.objects.filter(school=scuola).all()
    corsi = corsi.select_related('classroom', 'day_of_the_week', 'school')
    return render(request, template_name="school/school_detail.html", context={'scuola': scuola, 'corsi': corsi})