from django.shortcuts import render
from rest_framework import viewsets
from .models import MovieData
from .serializers import MovieDataSerializer


class MovieDataViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieDataSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre="action")
    serializer_class = MovieDataSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre="comedy")
    serializer_class = MovieDataSerializer


class DramaViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre="drama")
    serializer_class = MovieDataSerializer
