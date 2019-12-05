# cal/urls.py

from django.conf.urls import url
from . import views

app_name = 'ourCalendar'
urlpatterns = [
    url('test', views.CalendarView.as_view(), name='ourCalendar'),  # here
    # url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='ourCalendar2'),  # here
    url(r'^calendar2/$', views.CalendarViewSingleUser.as_view(), name='singleUser'),  # here
    url(r'^userCalendar/$', views.CalendarView.as_view(), name='ourUserCalendar'),  # here
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]
