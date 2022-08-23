from django.db import models

# Create your models here.

class Elevator(models.Model):
    # direction = models.CharField(max_length=4, choices=[('Up', 'Up'), ('Down', 'Down')])
    doorStatus = models.CharField(max_length=6, choices=[('Open', 'Open'), ('Closed', 'Closed')])
    currentFloor = models.IntegerField()
    motion = models.CharField(max_length=7, choices=[('Moving', 'Moving'), ('Stopped', 'Stopped')])
    operational = models.BooleanField(default=True)
    listofRequest = models.TextField(default='',blank=True, null=True)

