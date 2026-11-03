from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import School


class SchoolDetailView(DetailView):
    model = School


class SchoolListView(ListView):
    model = School