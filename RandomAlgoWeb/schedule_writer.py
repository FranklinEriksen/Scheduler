from accounts.models import empInfo
from django.utils.dateparse import parse_time
from .models import *
import RandomAlgoWeb.RandomAlgo.Algorithms as alg

def write_schedule(request):
    sch = alg.runUntilCorrectWithUsers(list(empInfo.objects.all()))
    Shift.objects.all().delete()

    for user in sch.users:
        for day in user.workDays:
            s = Shift(
                username = user.name,
                day = day.dayNumber,
                start_time = parse_time('0:00'),
                end_time = parse_time('0:00')
            )
            s.save()






