from django.shortcuts import render

from rest_framework import viewsets, generics
from .serializers import ArtisteSerializer, SongSerializer
from .models import Artiste, Song, Lyric


# Create your views here.
class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ArtisteList(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class ArtisteDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer


# class Artisteapi(viewsets.ModelViewSet):
#     queryset = Artiste.objects.all()
#     serializer_class = ArtisteSerializer
#     # http_method_names = ['get', 'post', 'retrieve', 'put', 'patch']

# class Songapi(viewsets.ModelViewSet):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer