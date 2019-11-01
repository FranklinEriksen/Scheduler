from django.db import models

# Create your models here.

#models.py File

class empInfo(models.Model):
    Name = models.CharField(max_length=300, unique=True)
