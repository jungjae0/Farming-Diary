from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from calendarapp.models import Event


class AllEventsListView(LoginRequiredMixin,ListView):
    """ All event list views """
    login_url = "accounts:signin"
    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_all_events(user=self.request.user)


class RunningEventsListView(LoginRequiredMixin,ListView):
    """ Running events list view """
    login_url = "accounts:signin"
    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_running_events(user=self.request.user)

class ExpectedEventsListView(LoginRequiredMixin,ListView):
    """ Running events list view """
    login_url = "accounts:signin"
    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_expected_events(user=self.request.user)