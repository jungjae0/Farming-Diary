from django.urls import path

from . import views

app_name = "calendarapp"


urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("calender/", views.CalendarViewNew.as_view(), name="calendar"),
    path("event/new/", views.create_event, name="event_new"),
    path("event/newitem/", views.create_item, name="item_new"),
    path("event/edit/<int:pk>/", views.EventEdit.as_view(), name="event_edit"),
    path("event/<int:event_id>/details/", views.event_details, name="event-detail"),
    path(
        "event/<int:pk>/remove",
        views.EventDeleteView.as_view(),
        name="remove_event",
    ),
    path("all-event-list/", views.AllEventsListView.as_view(), name="all_events"),
    path(
        "running-event-list/",
        views.RunningEventsListView.as_view(),
        name="running_events",
    ),
]
