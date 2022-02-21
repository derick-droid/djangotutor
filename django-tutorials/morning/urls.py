from django.urls import path
from . import views

urlpatterns =[
    path("days", views.displayfor, name="days"),
    path("good", views.good, name="good"),
    path("greet", views.greet, name="greet"),
    path("date", views.date, name="date"),
    path("redirect", views.redirect, name = "redirect"),
    path("<str:articleId>/", views.viewArticle, name = "viewarticle"),
   ]