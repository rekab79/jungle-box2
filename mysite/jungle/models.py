from django.db import models
import datetime

class GrowProfile(models.Model):

    temperature = models.FloatField()
    humidity = models.FloatField()
    species = models.CharField(max_length=250)
    plant_date = models.DateField(null=True,blank=True)
    name = models.CharField(max_length=25)

    
