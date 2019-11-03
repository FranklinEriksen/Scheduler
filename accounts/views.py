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
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post=Post()
            post.title= request.POST.get('title')
            post.content= request.POST.get('content')
            post.save()

            return render(request, 'posts/create.html')

        else:
            return render(request,'posts/create.html')


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
