from django.urls import path
from . import views

urlpatterns = [
    path("welcome/", views.welcome, name="welcome"),
    path("home/", views.home, name="home"),
    path("crudop/", views.crudops, name="crudop"),
    path("page/", views.page, name = "page"),
    path("hope/", views.hope, name="hope"),
    path("diva/", views.diva, name="diva"),
    path("studios/", views.studios, name = "studios"),
    path("<str:name>/", views.name, name="name"),
]
