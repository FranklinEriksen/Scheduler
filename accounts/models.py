from django.db import models
from django.db.models import CharField, Model

#models.py File


class empInfo(models.Model):
    Name = models.CharField(max_length=300, default='')
    Firstname = models.CharField(max_length=300, default='')
    Lastname = models.CharField(max_length=300, default='')
    Email = models.CharField(max_length=300, default='')
    Companyname = models.CharField(max_length=300, default='')

    Password = models.CharField(max_length=300, default = '')

    days = models.CharField(max_length=300, default = '11111111')

    #These are all strings, 24 bit binary string. Represents which hours of the day a person will be working
    #One for each day of the week
    mon = models.CharField(max_length=24, default = '000000000000000000000000')
    tues = models.CharField(max_length=24, default = '000000000000000000000000')
    wed = models.CharField(max_length=24, default = '000000000000000000000000')
    thurs = models.CharField(max_length=24, default = '000000000000000000000000')
    fri = models.CharField(max_length=24, default = '000000000000000000000000')
    sat = models.CharField(max_length=24, default = '000000000000000000000000')
    sun = models.CharField(max_length=24, default = '000000000000000000000000')

'''
-name
-For each of 7 days: 1/0 if they work
    -Default is that they work all day
'''
