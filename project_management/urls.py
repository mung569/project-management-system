from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_management, name="project_management"),
    path("home/", views.home, name="home"),
]