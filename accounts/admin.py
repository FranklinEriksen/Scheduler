from django.contrib import admin
from .models import empInfo
from .models import currentUser

# Register your models here.
admin.site.register(empInfo)
admin.site.register(currentUser)