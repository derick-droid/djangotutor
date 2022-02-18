from django.urls import path
from . import views

urlpatterns = [
    path("welcome/", views.welcome, name="welcome"),
    path("home/", views.home, name="home"),
    path("<str:name>/", views.name, name="name")
]
