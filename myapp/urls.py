from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("gestione/", views.gestione, name="gestione"),
    path("consulenza/", views.consulenza, name="consulenza"),
]

