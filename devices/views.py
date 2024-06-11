from django.shortcuts import render
from .models import CollectedData
from .serializers import CollectedDataSerializer
from rest_framework import viewsets

class CollectedDataViewset(viewsets.ModelViewSet):
    queryset = CollectedData.objects.all()
    serializer_class = CollectedDataSerializer
    