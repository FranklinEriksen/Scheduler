from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from django.utils.dateparse import parse_datetime
from RandomAlgoWeb.RandomAlgo.Main import runUntilCorrect as algo
from RandomAlgoWeb.RandomAlgo.ListHolder import Listholder

from .models import *
from .utils import Calendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'ourCalendar/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the ourCalendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our ourCalendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our ourCalendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['ourCalendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def insert_test(listholder):

    for user in listholder.users:
        for day in user.workDays:
            Event.objects.create(title=user.ID,
                                 description=user.job,
                                 start_time=parse_datetime('2019-10-' + str(day.date) + 'T19:00:00'),
                                 end_time=parse_datetime('2019-10-' + str(day.date) + 'T19:00:00'))



    # test = Event.objects.create(title='Frederik',
    #                             description='Not Sure',
    #                             start_time=parse_datetime('2019-10-31T19:00:00'),
    #                             end_time=parse_datetime('2019-10-31T19:00:00'))