from django.db import models

# Create your models here.

class DLModel(models.Model):
    name = models.TextField(max_length=50)
    version = models.TextField(max_length=30)
    
