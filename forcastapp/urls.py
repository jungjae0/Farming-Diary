from django.urls import path
from . import views

app_name = "forcastapp"

urlpatterns = [
    # path('', views.index, name="home"),
    path("", views.result, name="result"),
    # path('social_links', views.social_links),
]
