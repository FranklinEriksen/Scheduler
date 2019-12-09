from django.urls import path

from . import views

app_name = 'algorithm'
urlpatterns = [
    path('run/', views.run_Algorithm, name='run'),
]