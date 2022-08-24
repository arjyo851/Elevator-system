from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Elevator(models.Model):
    doorStatus = models.CharField(max_length=6, choices=[('Open', 'Open'), ('Closed', 'Closed')])
    currentFloor = models.IntegerField()
    motion = models.CharField(max_length=7, choices=[('Moving', 'Moving'), ('Stopped', 'Stopped')])
    operational = models.BooleanField(default=True)
    listofRequest = ArrayField(models.IntegerField(default=list, blank=True,null=True), blank=True,null=True)


