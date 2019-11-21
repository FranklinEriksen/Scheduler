from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

import RandomAlgoWeb.RandomAlgo.Algorithms as Algorithms
import RandomAlgoWeb.RandomAlgo.Utils as algo
from django.http import HttpResponse
import datetime
from accounts.models import empInfo
from django.utils.dateparse import parse_datetime
from .models import *


def run_Algorithm(request):
    test = Algorithms.runUntilCorrectWithUsers(list(empInfo.objects.all()))
    html = "<html><body>"
    for x in test.days:
        html += "Day " + str(x.dayNumber) + ", workers are : " + x.usersForTheDayToString()
        html += "<br />"
    html += "</body></html>"

    insert_test_DB(test)

    return HttpResponse(html)


def insert_test_DB(listHolder):
    CalculatedCalendar.objects.all().delete()
    for user in listHolder.users:
        for day in user.workDays:
            CalculatedCalendar.objects.create(title=str(user.name) + " is working as  " + str(user.job.toString()),
                                              description=user.job,
                                              start_time=parse_datetime('2019-11-' + str(day.date) + 'T19:00:00'),
                                              end_time=parse_datetime('2019-11-' + str(day.date) + 'T19:00:00'),
                                              name=str(user.name))