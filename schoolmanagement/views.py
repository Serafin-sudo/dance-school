from django.shortcuts import render
from django.views.generic import DetailView, ListView
from schoolmanagement.models import School

class SchoolDetailView(DetailView):
    model = School


class SchoolListView(ListView):
    model = School


"""
class SchoolDetailView(DetailView):
    scuole=School.objects.all()
    return render(
        request,
        template_name="schoolmanagement/school_list.html",
        context={"object_list":scuole}
    )
"""