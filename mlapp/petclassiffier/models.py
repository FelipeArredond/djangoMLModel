from platform import architecture
from django.db import models

# Create your models here.

class mlModels(models.Model):
    tittle = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    architecture = models.FileField(upload_to='mlmodel/')
    weigths = models.FileField(upload_to='mlmodel/')
    priority = models.PositiveSmallIntegerField(null = True)
