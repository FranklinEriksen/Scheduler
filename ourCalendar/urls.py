# cal/urls.py

from django.conf.urls import url
from . import views

app_name = 'ourCalendar'
urlpatterns = [
    # url(r'^index/$', views.index, name='index'),
    url('test', views.CalendarView.as_view(), name='ourCalendar'), # here
    url(r'^calendar/$', views.CalendarView.as_view(), name='ourCalendar'),  # here
]