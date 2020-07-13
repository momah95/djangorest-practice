from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero
from rest_framework import generics

# Create your views here.
class HeroView(generics.ListCreateAPIView):
    #This class defines the create behavior of our rest api.
    queryset = Hero.objects.all().order_by('id')
    serializer_class = HeroSerializer

    def perform_create(self, serializer):
        #Save the post data when creating a new hero.
        serializer.save()