from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SkillsModel
from .serializers import SkillSerializer
# Create your views here.

@api_view(['GET'])
def allAPIView(request):
    api_urls = {
        'List' : '/list/',
        'Create': '/create/',
        'Detail': '/detail/<int:pk>/',
        'Update': '/update/<int:pk>/',
        'Delete' : '/delete/<int:pk>/',
    }
    return Response(api_urls)

class SkillListView(generics.ListAPIView):
    queryset = SkillsModel.objects.all()
    serializer_class = SkillSerializer

class SkillsCreateView(generics.CreateAPIView):
    queryset = SkillsModel.objects.all()
    serializer_class = SkillSerializer

class SkillsDetailView(generics.RetrieveAPIView):
    queryset = SkillsModel.objects.all()
    serializer_class = SkillSerializer

class SkillsUpdateView(generics.UpdateAPIView):
    queryset = SkillsModel.objects.all()
    serializer_class = SkillSerializer

class SkillsDeleteView(generics.DestroyAPIView):
    queryset = SkillsModel.objects.all()
    serializer_class = SkillSerializer

