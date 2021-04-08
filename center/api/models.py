from django.db import models

# Create your models here.
class Model_DL(models.Model):
    version_model = models.CharField(max_length=255)
    url_model = models.CharField(max_length=255)

    def __str__(self):
        return self.version_model