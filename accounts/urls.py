# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('companysignup/', views.SignUpComp.as_view(), name='signup-company'),
    path('employeesignup/', views.SignUpEmp.as_view(), name='signup-employee'),
]
