# from django.urls import path
from .views import ArtisteViewSet, SongViewSet, LyricViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(
    'artisteviewset', ArtisteViewSet, basename='artiste'
)

router.register(
    'songviewset', SongViewSet, basename='song',
)

router.register(
    'lyricviewset', LyricViewSet, basename='lyric',
)

urlpatterns = [
    # path("home", ArtisteViewSet, name ')
]+router.urls
