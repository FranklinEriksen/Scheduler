from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

import RandomAlgoWeb.RandomAlgo.Algorithms
import RandomAlgoWeb.RandomAlgo.Utils as algo
from django.http import HttpResponse
import datetime
from ourCalendar.views import insert_test_DB
from accounts.models import empInfo


class FrederikTest(generic.CreateView):
    test = RandomAlgoWeb.RandomAlgo.Algorithms.runUntilCorrect()
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def current_datetime(request):
    nytest = list(empInfo.objects.all())
    test = RandomAlgoWeb.RandomAlgo.Algorithms.runUntilCorrectWithUsers(list(empInfo.objects.all()))
    html = "<html><body>"

    for x in test.days:
        html += "Day " + str(x.dayNumber) + ", workers are : " + x.usersForTheDayToString()
        html += "<br />"
    html += "</body></html>"

    insert_test_DB(test)

    return HttpResponse(html)