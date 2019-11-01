# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import empInfo


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

def saveinfo(request):
        print("THIS GOT HITTTT")
        if request.method == 'submitInfo':
            if request.POST.get('namebox'):
                db=empInfo()
                db.Name= request.submitInfo.get('namebox')
                db.save()
