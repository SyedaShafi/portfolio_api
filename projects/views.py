from django.shortcuts import render
from rest_framework import generics
from . models import ProjectModel
from . serializers import ProjectsSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
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


class ProjectListView(generics.ListAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectsSerializers

class ProjectCreateView(generics.CreateAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectsSerializers


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectsSerializers

class ProjectUpdateView(generics.UpdateAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectsSerializers

class ProjectDeleteView(generics.DestroyAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectsSerializers


