from django.urls import path

from . import views


urlpatterns = [
    path('FrederikTest/', views.FrederikTest.as_view(), name='test'),
    path('time/', views.current_datetime, name='time'),
]