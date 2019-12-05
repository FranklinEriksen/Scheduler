from django.db import models

# Create your models here.


class CalculatedCalendar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    name = models.CharField(max_length=200)

# Store data of who is working when
class Shift(models.Model):
    username = models.CharField(max_length=127)
    day = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
