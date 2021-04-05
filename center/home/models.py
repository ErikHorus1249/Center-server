from django.db import models

# Create your models here.

class DLModel(models.Model):
    name = models.TextField()
    version = models.TextField()
    
