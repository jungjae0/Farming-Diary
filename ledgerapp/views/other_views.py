from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta, datetime, date
import calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse


from ledgerapp.models import Ledger
from ledgerapp.utils import Calendar
from ledgerapp.forms import LedgerForm


from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


@login_required(login_url="signup")
def create_ledger(request):
    form = LedgerForm(request.POST or None)
    if request.POST and form.is_valid():
        date = form.cleaned_data["date"]
        type = form.cleaned_data["type"]
        item = form.cleaned_data["item"]
        business = form.cleaned_data["business"]
        category = form.cleaned_data["category"]
        correspondent = form.cleaned_data["correspondent"]
        amount = form.cleaned_data["amount"]
        payment = form.cleaned_data["payment"]
        description = form.cleaned_data["description"]
        Ledger.objects.get_or_create(
            user=request.user,
            date=date,
            type=type,
            item=item,
            business=business,
            category=category,
            correspondent=correspondent,
            amount=amount,
            payment=payment,
            description=description,
        )
        return HttpResponseRedirect(reverse("ledgerapp:dashboard"))
    return render(request, "ledger.html", {"form": form })


class LedgerEdit(generic.UpdateView):
    model = Ledger
    fields = ["date", "type", "item", "business","category", "correspondent", "amount", "payment", "description"]
    template_name = "ledger.html"
    # success_url = reverse_lazy("ledgerapp:calendar")


@login_required(login_url="signup")
def ledger_details(request, ledger_id):
    ledger = Ledger.objects.get(id=ledger_id)
    context = {"ledger": ledger}
    return render(request, "ledger-details.html", context)



class LedgerDeleteView(generic.DeleteView):
    model = Ledger
    template_name = "ledger-delete.html"
    success_url = reverse_lazy("ledgerapp:dashboard")


class LedgerViewNew(LoginRequiredMixin, generic.View):
    login_url = "accounts:signin"
    template_name = "ledgerapp/dashboard.html"
    form_class = LedgerForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        ledgers = Ledger.objects.get_income_ledgers(user=request.user)
        ledgers_month = Ledger.objects.get_outcome_ledgers(user=request.user)
        ledger_list = []
        # start: '2020-09-16T16:00:00'
        for ledger in ledgers:
            ledger_list.append(
                {
                    # "title": ledger.title,
                    "date": ledger.date.strftime("%Y-%m-%d"),
                    "type": ledger.type,
                    "item": ledger.item,
                    "business": ledger.business,
                    "correspondent": ledger.correspondent,
                    "amount": ledger.amount,
                    "payment": ledger.payment,
                    "description": ledger.description,



                }
            )
        context = {"form": forms, "ledgers": ledger_list,
                   "ledgers_month": ledgers_month}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("ledgerapp:calendar")
        context = {"form": forms}
        return render(request, self.template_name, context)


class DashboardView(LoginRequiredMixin, View):
    login_url = "accounts:signin"
    template_name = "ledgerapp/dashboard.html"

    def get(self, request, *args, **kwargs):
        year = date.today().year
        month = date.today().month
        ledgers = Ledger.objects.filter(date__year=year, date__month=month, user=request.user)
        income = Ledger.objects.filter(date__year=year,type='수입', date__month=month, user=request.user)
        outcome = Ledger.objects.filter(date__year=year,type='지출', date__month=month, user=request.user)
        context = {
            "month": month,
            "total_ledger": ledgers,
            "income": income,
            "outcome": outcome,
        }
        return render(request, self.template_name, context)


# Event.objects.get_all_events(user=request.user)