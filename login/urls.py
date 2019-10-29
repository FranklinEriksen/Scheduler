from django.urls import path

from . import views

from django.urls import path

from . import views

urlpatterns = [
    path('login2', views.Login.as_view(), name='login2'),
]
