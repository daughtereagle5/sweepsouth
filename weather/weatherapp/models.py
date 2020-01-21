from django.db import models

# Create your models here.
class CurrentLocation(models.Model):
    date = models.DateTimeField()
    typeday = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    temp = models.FloatField()
    windspeed = models.FloatField()
    windbearing = models.FloatField()
    windgust = models.FloatField()
    rain_prob = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class BookingLocation(models.Model):
    date = models.DateTimeField()
    typeday = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    temp = models.FloatField()
    windspeed = models.FloatField()
    windbearing = models.FloatField()
    windgust = models.FloatField()
    rain_prob = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()