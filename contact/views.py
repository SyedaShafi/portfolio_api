from django.shortcuts import render
from rest_framework import generics
from .serializers import ContactSerializers
from .models import ContactModel
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def allAPIView(request):
    api_urls = {
        'List' : '/list/',
        'Create': '/create/',
    }
    return Response(api_urls)


# Create your views here.
class ContactListView(generics.ListAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializers

class ContactCreateView(generics.CreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializers
    

    def perform_create(self, serializer):
        instance = serializer.save()
        subject = f'{instance.name} Send you a mail'
        message =   message = f"Name: {instance.name}\nEmail: {instance.email}\nMessage:\n{instance.message}"
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

