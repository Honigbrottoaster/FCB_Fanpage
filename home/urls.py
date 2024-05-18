from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("galerie/", views.galerie, name="galerie"),
    path("review/", views.review, name="review"),
]