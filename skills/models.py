from django.db import models

# Create your models here.
class SkillsModel(models.Model):
    src = models.ImageField(upload_to='skills/images/')
    title = models.CharField(max_length=100)
    style = models.CharField(max_length=200)