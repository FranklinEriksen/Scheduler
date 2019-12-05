# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('loginNew/', views.loginNew.as_view(), name = 'loginNew'),
    path('viewschedule/', views.viewschedule.as_view(), name = 'viewschedule'),
    path('myAccount/', views.myAccount.as_view(), name = 'myAccount'),
    path('companysignup/', views.SignUpComp.as_view(), name='signup-company'),
    path('employeesignup/', views.SignUpEmp.as_view(), name='signup-employee'),
    path('employeeViewSched/', views.ViewSchedEmp.as_view(), name='ViewSched-employee' ),
    path('avail/', views.Avail.as_view(), name='avail' ),
    path('viewSched/', views.viewSched.as_view(), name='viewSched' ),
    path('submitInfo/', views.availability, name="submitInfo"),
    path('trylogin/', views.trylogin, name="trylogin")
]
