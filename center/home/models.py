from django.db import models

# Create your models here.

class DLModel(models.Model):
    modelUrl = models.TextField(max_length=100)
    modelVersion = models.TextField(max_length=30)
    
