from django.urls import path, include
from . import views

# These are the urls for your music app
urlpatterns = [
    path("song/", views.SongList.as_view()),
    path("song/<int:pk>", views.SongDetail.as_view()),
    path("artiste/", views.ArtisteList.as_view()),
    path("artiste/<int:pk>", views.ArtisteDetails.as_view())
]