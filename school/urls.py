from django.urls import path
from school import views

urlpatterns = [
    path("<int:pk>/", views.scuola, name="scuola"),
]