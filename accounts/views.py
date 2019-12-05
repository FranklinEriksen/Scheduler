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
            try:
                returnStr = getHours(request.GET['monday-start'], request.GET['monday-end'] )
            except:
                returnStr = "000000000000000000000000"
            db.mon = returnStr
        else:
            daysString+='0'

        if 'tuesday' in request.GET:
            daysString+='1'
            try:
                returnStr = getHours(request.GET['tuesday-start'], request.GET['tuesday-end'] )
            except:
                returnStr = "000000000000000000000000"
            db.tues = returnStr
        else:
            daysString+='0'

        if 'wednesday' in request.GET:
            daysString+='1'
            try:
                returnStr = getHours(request.GET['wednesday-start'], request.GET['wednesday-end'] )
            except:
                returnStr = "000000000000000000000000"
            db.wed = returnStr
        else:
            daysString+='0'

        if 'thursday' in request.GET:
            daysString+='1'
            try:
                returnStr = getHours(request.GET['thursday-start'], request.GET['thursday-end'] )
            except:
                returnStr = "000000000000000000000000"
            db.thurs = returnStr
        else:
            daysString+='0'

        if 'friday' in request.GET:
            daysString+='1'
            try:
                returnStr = getHours(request.GET['friday-start'], request.GET['friday-end'] )
            except:
                returnStr = "000000000000000000000000"
            db.fri = returnStr
        else:
            daysString+='0'

        if 'saturday' in request.GET:
            daysString+='1'
            try:
                returnStr = getHours(request.GET['saturday-start'], request.GET['saturday-end'] )
            except:
                returnStr = "000000000000000000000000"
            db.sat = returnStr
        else:
            daysString+='0'

        if 'sunday' in request.GET:
            daysString+='1'
            try:
                returnStr = getHours(request.GET['sunday-start'], request.GET['sunday-end'] )
            except:
                returnStr = "000000000000000000000000"
            db.sun = returnStr
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

    def get_context_data(self, **kwargs):
        Name = "Name will go here"
        print("HERE IS THE NAME", Name)
        context= {
            'Name': Name,
        }
        return context

class Avail(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('Avail')
    template_name = 'availability.html'

class viewSched(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('viewSched')
    template_name = 'ourCalendar/calendar.html'

class loginNew(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('loginNew')
    template_name = 'loginNew.html'

class myAccount(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('myAccount')
    template_name = 'myaccount.html'

    def get_context_data(self, **kwargs):
        firstname = "FIRSTNAME"
        lastname = "LASTNAME"
        role = "ROLE"
        context= {
            'firstname': firstname,
            'lastname' : lastname,
            'role' : role,
        }
        return context

class viewschedule(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('viewschedule')
    template_name = 'view-schedule.html'
