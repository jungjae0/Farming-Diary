from django.urls import path
from . import views

app_name = "weatherapp"

urlpatterns = [
    path('tavg/', views.tavg, name='temp-graph'),
    path('thum/', views.thum, name='humid-graph'),
    path('trainfall/', views.trainfall, name='rainfall-graph'),
    path('insolation/', views.sunshine, name='insolation-graph'),
    # path('yesterday/', views.tavg, name='yesterday'),
]