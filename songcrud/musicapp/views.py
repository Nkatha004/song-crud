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