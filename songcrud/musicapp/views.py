<<<<<<< HEAD
from .models import Artiste, Song, Lyric
from rest_framework import serializers, viewsets
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer

# Create your views here.

class ArtisteViewSet(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class LyricViewSet(viewsets.ModelViewSet):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> a8cc677efe39809d1850f1597a1602110a2a77b4
