from django.db import models

# Create your models here.

#models.py File

class empInfo(models.Model):
    Name = models.CharField(max_length=300)
    days = models.CharField(max_length=300, default = '11111111')

'''
-name
-For each of 7 days: 1/0 if they work
    -Default is that they work all day
'''
