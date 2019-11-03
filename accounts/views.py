# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import empInfo

def availability(request):
    daysString = ''
    db=empInfo()

    if request.method == 'GET':
        if 'namebox' in request.GET:
            print(request.GET['namebox'])
            db.Name = (request.GET['namebox'])

        if 'monday' in request.GET:
            daysString+='1'
        else:
            daysString+='0'

        if 'tuesday' in request.GET:
            daysString+='1'
        else:
            daysString+='0'

        if 'wednesday' in request.GET:
            daysString+='1'
        else:
            daysString+='0'

        if 'thursday' in request.GET:
            daysString+='1'
        else:
            daysString+='0'

        if 'friday' in request.GET:
            daysString+='1'
        else:
            daysString+='0'

        if 'saturday' in request.GET:
            daysString+='1'
        else:
            daysString+='0'

        if 'sunday' in request.GET:
            daysString+='1'
        else:
            daysString+='0'

        db.days = daysString
        db.save()

        print(daysString)

    return render(request,'../templates/availability.html')


class SignUpComp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signup-company')
    template_name = 'signup-company.html'

class SignUpEmp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signup-employee')
    template_name = 'signup-employee.html'

class ViewSchedEmp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('ViewSched-employee')
    template_name = 'view-schedule.html'

class Avail(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('Avail')
    template_name = 'availability.html'
