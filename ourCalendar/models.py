from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    name = models.CharField(max_length=200, default='TEST')

    @property
    def get_html_url(self):
        url = reverse('ourCalendar:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


