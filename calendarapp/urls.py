from django.urls import path

from . import views

app_name = "calendarapp"


urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("calender/", views.CalendarView.as_view(), name="calendar"),
    path("event/new/", views.create_event, name="event-new"),
    path("event/newitem/", views.create_item, name="item-new"),
    path("event/edit/<int:pk>/", views.EventEdit.as_view(), name="event-edit"),
    path("event/<int:event_id>/details/", views.event_details, name="event-detail"),
    path(
        "event/<int:pk>/remove",
        views.EventDeleteView.as_view(),
        name="event-remove",
    ),
    path("all-event-list/", views.AllEventsListView.as_view(), name="all-events"),
    path(
        "running-event-list/",
        views.RunningEventsListView.as_view(),
        name="running_events",
    ),
]
