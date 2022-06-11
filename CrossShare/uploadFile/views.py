from django.shortcuts import render
from .models import uploadFile
from .serializer import fileSerializer
from rest_framework import generics
# Create your views here.

class fileListCreateView(generics.ListCreateAPIView):
    queryset = uploadFile.objects.all()
    serializer_class= fileSerializer


class fileRetreiveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = uploadFile.objects.all()
    serializer_class= fileSerializer
