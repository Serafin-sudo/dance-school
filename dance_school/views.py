from django.http import HttpResponse

def test_view(request):
    return HttpResponse("View di prova con HttpResponse")