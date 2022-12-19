from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from ledgerapp.models import Ledger

class AllLedgersListView(LoginRequiredMixin, ListView):
    """ All event list views """
    login_url = "accounts:signin"
    template_name = "ledgerapp/ledgers_list.html"
    model = Ledger

    def get_queryset(self):
        return Ledger.objects.get_all_ledgers(user=self.request.user)


class IncomeLedgersListView(LoginRequiredMixin, ListView):
    """ All event list views """
    login_url = "accounts:signin"
    template_name = "ledgerapp/ledgers_list.html"
    model = Ledger

    def get_queryset(self):
        return Ledger.objects.get_income_ledgers(user=self.request.user)


class OutcomeLedgersListView(LoginRequiredMixin, ListView):
    """ Running events list view """
    login_url = "accounts:signin"
    template_name = "ledgerapp/ledgers_list.html"
    model = Ledger

    def get_queryset(self):
        return Ledger.objects.get_outcome_ledgers(user=self.request.user)
