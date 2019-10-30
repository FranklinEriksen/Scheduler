from django.contrib import admin

# Register your models here.
from django.contrib import admin
from ourCalendar.models import Event

admin.site.register(Event)