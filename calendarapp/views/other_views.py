# cal/ledger.py
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta, datetime, date
import calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse


from calendarapp.models import Event, Item
from calendarapp.utils import Calendar
from calendarapp.forms import EventForm, ItemForm

# import pandas as pd
from datetime import datetime

from django.views.generic import View

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month


class CalendarView(LoginRequiredMixin, generic.ListView):
    login_url = "accounts:signin"
    model = Event
    template_name = "calendarapp/calendar.html"

    # template_name = "calendarapp:calendar"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True, user=self.request.user)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        context["running_events"] = self.model.objects.get_running_events(user=self.request.user)
        context["expected_events"] = self.model.objects.get_expected_events(user=self.request.user)
        # context["user"] = self.model.objects.all()
        return context


@login_required(login_url="signup")
def create_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data["title"]
        start_time = form.cleaned_data["start_time"]
        end_time = form.cleaned_data["end_time"]
        item = form.cleaned_data["item"]
        description = form.cleaned_data["description"]
        active = form.cleaned_data["active"]
        image = request.FILES.get('image')
        level = form.cleaned_data["level"]
        Event.objects.get_or_create(
            user=request.user,
            title = title,
            start_time=start_time,
            end_time=end_time,
            item=item,
            description=description,
            active=active,
            image=image,
            level=level,
        )
        return HttpResponseRedirect(reverse("calendarapp:calendar"))
    return render(request, "calendarapp/new-event.html", {"form": form})

@login_required(login_url="signup")
def create_item(request):
    form = ItemForm(request.POST or None)
    if request.POST and form.is_valid():
        item = form.cleaned_data["item"]
        Item.objects.get_or_create(
            # user=request.user,
            item = item
        )
        return HttpResponseRedirect(reverse("calendarapp:event-new"))
    return render(request, "calendarapp/calendar-item.html", {"form": form})

class EventEdit(generic.UpdateView):
    model = Event
    fields = ["title","start_time", "end_time", "item", "description", "active", "image", "level"]
    template_name = "calendarapp/event-edit.html"
    success_url = reverse_lazy("calendarapp:calendar")

# class EventDeleteView(generic.DeleteView):
#     model = Event
#     template_name = "calendarapp/event_delete.html"
#     success_url = reverse_lazy("calendarapp:calendar")

def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    # post = event.post
    if request.user.is_authenticated:
        event.delete()
        return redirect(event.get_absolute_url2())
    else:
        raise PermissionDenied

def delete_event1(request, pk):
    event = get_object_or_404(Event, pk=pk)
    # post = event.post
    if request.user.is_authenticated:
        event.delete()
        return redirect(event.get_absolute_url3())
    else:
        raise PermissionDenied


@login_required(login_url="signup")
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {"event": event }
    return render(request, "calendarapp/event-details.html", context)

class DashboardView(LoginRequiredMixin, View):
    login_url = "accounts:signin"
    template_name = "calendarapp/dashboard.html"

    def get(self, request, *args, **kwargs):
        events = Event.objects.get_all_events(user=request.user)
        running_events = Event.objects.get_running_events(user=request.user)
        expected_events = Event.objects.get_expected_events(user=request.user)
        latest_events = Event.objects.filter(user=request.user).order_by("-id")[:10]
        end_evnets = events.count() - running_events.count() - expected_events.count()
        context = {
            "total_event": events.count(),
            "running_events": running_events,
            "latest_events": latest_events,
            "expected_events": expected_events,
            "end_events": end_evnets
        }
        return render(request, self.template_name, context)

# class CalendarViewNew(LoginRequiredMixin, generic.View):
#     login_url = "accounts:signin"
#     template_name = "calendarapp/calendar.html"
#     form_class = EventForm
#
#     def get(self, request, *args, **kwargs):
#         forms = self.form_class()
#         events = Event.objects.get_all_events(user=request.user)
#         events_month = Event.objects.get_running_events(user=request.user)
#         event_list = []
#         # start: '2020-09-16T16:00:00'
#         for event in events:
#             event_list.append(
#                 {
#                     "title": event.title,
#                     "item": event.item,
#                     "description": event.description,
#                     "active": event.active,
#                     "image": event.image,
#                     "level": event.level,
#                     "start": event.start_time.strftime("%Y-%m-%dT%H:%M:%S"),
#                     "end": event.end_time.strftime("%Y-%m-%dT%H:%M:%S"),
#
#                 }
#             )
#         context = {"form": forms, "events": event_list,
#                    "events_month": events_month}
#         return render(request, self.template_name, context)
#
#     def post(self, request, *args, **kwargs):
#         forms = self.form_class(request.POST)
#         if forms.is_valid():
#             form = forms.save(commit=False)
#             form.user = request.user
#             form.save()
#             return redirect("calendarapp:calendar")
#         context = {"form": forms}
#         return render(request, self.template_name, context)