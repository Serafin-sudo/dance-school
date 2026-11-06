from django.urls import path
from school import views

urlpatterns = [
    path("<int:pk>/", views.scuola, name="scuola"),
    # corso
    path("corso/nuovo/", views.CourseCreateView.as_view(), name="nuovo-corso"),
    path("corso/<int:pk>/modifica/", views.CourseUpdateView.as_view(), name="modifica-corso"),
    # aula
    path("aula/nuovo/", views.ClassroomCreateView.as_view(), name="nuova-aula"),
    path("aula/<int:pk>/modifica/", views.ClassroomUpdateView.as_view(), name="modifica-aula"),
    # giorno della settimana
    path("giorno/nuovo/", views.DayCreateView.as_view(), name="nuovo-giorno"),
    path("giorno/<int:pk>/modifica/", views.DayUpdateView.as_view(), name="modifica-giorno"),
]