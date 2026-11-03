from django.http import HttpResponse
from django.shortcuts import render

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