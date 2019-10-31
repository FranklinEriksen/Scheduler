from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import RandomAlgoWeb.RandomAlgo.Main as algo
from django.http import HttpResponse
import datetime
from ourCalendar.views import insert_test


class FrederikTest(generic.CreateView):
    test = algo.runUntilCorrect()
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def current_datetime(request):
    test = algo.runUntilCorrect()
    now = datetime.datetime.now()
    html = "<html><body>"

    for x in test.days:
        html += "Day " + str(x.dayNumber) + ", workers are : " + x.usersForTheDayToString()
        html += "<br />"
    html += "</body></html>"

    insert_test(test)

    return HttpResponse(html)