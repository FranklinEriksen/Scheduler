# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('companysignup/', views.SignUpComp.as_view(), name='signup-company'),
    path('employeesignup/', views.SignUpEmp.as_view(), name='signup-employee'),
    path('employeeViewSched/', views.ViewSchedEmp.as_view(), name='ViewSched-employee' ),
    path('avail/', views.Avail.as_view(), name='avail' ),

]
