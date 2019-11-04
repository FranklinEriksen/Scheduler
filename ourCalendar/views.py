from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from django.utils.dateparse import parse_datetime
from RandomAlgoWeb.RandomAlgo.Algorithms import runUntilCorrect as algo
from RandomAlgoWeb.RandomAlgo.ListHolder import Listholder

from .models import *
from .forms import *
from .utils import Calendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'ourCalendar/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('month', None))

        # Instantiate our ourCalendar class with today's year and date
        cal = Calendar(d.year, d.month)

        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)


        # Call the formatmonth method, which returns our ourCalendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['ourCalendar'] = mark_safe(html_cal)
        return context


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('ourCalendar:ourCalendar'))
    return render(request, 'ourCalendar/event.html', {'form': form})


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def insert_test(listholder):

    for user in listholder.users:
        for day in user.workDays:
            Event.objects.create(title=str(user.ID) + " is working as  " + str(user.job.toString()),
                                 description=user.job,
                                 start_time=parse_datetime('2019-10-' + str(day.date) + 'T19:00:00'),
                                 end_time=parse_datetime('2019-10-' + str(day.date) + 'T19:00:00'))

def insert_test_DB(listholder):
    Event.objects.all().delete()
    for user in listholder.users:
        for day in user.workDays:
            Event.objects.create(title=str(user.name) + " is working as  " + str(user.job.toString()),
                                 description=user.job,
                                 start_time=parse_datetime('2019-11-' + str(day.date) + 'T19:00:00'),
                                 end_time=parse_datetime('2019-11-' + str(day.date) + 'T19:00:00'))

    # test = Event.objects.create(title='Frederik',
    #                             description='Not Sure',
    #                             start_time=parse_datetime('2019-10-31T19:00:00'),
    #                             end_time=parse_datetime('2019-10-31T19:00:00'))
