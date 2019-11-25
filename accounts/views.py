# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import empInfo

import ourCalendar

def getHours(startTime, endTime):
    
    if startTime.isnumeric() == False or endTime.isnumeric() == False:
        return "000000000000000000000000"


    startHour = int(startTime[:2])
    endHour = int(endTime[:2])

    if endHour < startHour:
        return "000000000000000000000000"

    str = ""

    for i in range(0, 24):
        if i >= startHour and i <= endHour:
            str += "1"
        else:
            str += "0"

    return str


def availability(request):
    #this will create a new database entry
    daysString = ''
    db=empInfo() # new data base instance

    #request.get is a dictionary
    if request.method == 'GET':
        if 'namebox' in request.GET: #namebox will only be in the request if there was text inside of it
            print(request.GET['namebox']) #for testing purposes, we print the name here
            db.Name = (request.GET['namebox']) #set the correct field in the database

        #Now, for each day of the week, add the number 1 if the person is working on that particular day
        #Will end up with a binary corresponding to the days
        if 'monday' in request.GET:
            daysString+='1'
            #returnStr = getHours(request.GET['monday-start'], request.GET['monday-end'] )
            #db.mon = returnStr
            #print (returnStr)
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

        #We then save the database
        db.days = daysString
        db.save()

        #Print the strings out for testing purposes
        print(daysString)

    return render(request,'../templates/availability.html')


#These are all farily normal views that just redirect to a certain HTML
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

class viewSched(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('viewSched')
    template_name = 'ourCalendar/calendar.html'
