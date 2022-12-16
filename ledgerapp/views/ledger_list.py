from django.views.generic import ListView

from ledgerapp.models import Ledger

class AllLedgersListView(ListView):
    """ All event list views """

    template_name = "ledgerapp/ledgers_list.html"
    model = Ledger

    def get_queryset(self):
        return Ledger.objects.get_all_ledgers(user=self.request.user)


class IncomeLedgersListView(ListView):
    """ All event list views """

    template_name = "ledgerapp/ledgers_list.html"
    model = Ledger

    def get_queryset(self):
        return Ledger.objects.get_income_ledgers(user=self.request.user)


class OutcomeLedgersListView(ListView):
    """ Running events list view """

    template_name = "ledgerapp/ledgers_list.html"
    model = Ledger

    def get_queryset(self):
        return Ledger.objects.get_outcome_ledgers(user=self.request.user)
