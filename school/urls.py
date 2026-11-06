from django.urls import path
from school import views

urlpatterns = [
    path("<int:pk>/", views.scuola, name="scuola"),
    path("corso/<int:pk>/modifica/", views.CourseUpdateView.as_view(), name="modifica-corso"),
    path("giorno/<int:pk>/modifica/", views.DayUpdateView.as_view(), name="modifica-giorno"),
    path("aula/<int:pk>/modifica/", views.ClassroomUpdateView.as_view(), name="modifica-aula"),
]