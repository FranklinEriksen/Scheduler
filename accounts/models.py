from django.db import models
#
# #models.py File
# class User(models.Model):
#     Password = models.IntegerField()
#     Email = models.CharField(max_length=300, default='')

class empInfo(models.Model):
    Name = models.CharField(max_length=300, default='')
    Firstname = models.CharField(max_length=300, default='')
    Lastname = models.CharField(max_length=300, default='')
    Password = models.CharField(max_length=300, default='')
    Email = models.CharField(max_length=300, default='')
    Username = models.CharField(max_length=300, default='')

    days = models.CharField(max_length=300, default = '11111111')

    #These are all strings, 24 bit binary string. Represents which hours of the day a person will be working
    #One for each day of the week
    mon = models.CharField(max_length=24, default = '111111111111111111111111')
    tues = models.CharField(max_length=24, default = '111111111111111111111111')
    wed = models.CharField(max_length=24, default = '111111111111111111111111')
    thurs = models.CharField(max_length=24, default = '111111111111111111111111')
    fri = models.CharField(max_length=24, default = '111111111111111111111111')
    sat = models.CharField(max_length=24, default = '111111111111111111111111')
    sun = models.CharField(max_length=24, default = '111111111111111111111111')

class currentUser(models.Model):
    currentUsername = models.CharField(max_length=300, default='')

# class Company(User):
#     Companyname = models.CharField(max_length=300, default='')
#     location = models.TextField()


'''
-name
-For each of 7 days: 1/0 if they work
    -Default is that they work all day
'''
