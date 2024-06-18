from django.db import models

# Create your models here.
class ProjectModel(models.Model):
    image = models.ImageField(upload_to='projects/images/')
    code_link = models.URLField(max_length=256)
    live_link = models.URLField(max_length=256)