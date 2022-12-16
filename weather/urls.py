from django.urls import path
from . import views

app_name = "weatherapp"

urlpatterns = [
    path('tavg/', views.tavg, name='temp-graph'),
    path('thum/', views.thum, name='humid-graph'),
]