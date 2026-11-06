from django.shortcuts import render
from django.views.generic import DetailView, ListView
from schoolmanagement.models import School

class SchoolListView(ListView):
    model = School
    

class SchoolDetailView(DetailView):
    model = School
    template_name = 'school/school_detail.html'