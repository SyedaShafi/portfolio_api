from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=140)
    email = models.EmailField()
    message = models.TextField()

    