from datetime import datetime
from django.db import models
from django.urls import reverse

from ledgerapp.models import LedgerAbstract
from accounts.models import User

class LedgerManager(models.Manager):

    """ Ledger manager """

    def get_all_ledgers(self, user):
        all_ledgers = Ledger.objects.filter(user=user)

        return all_ledgers

    def get_income_ledgers(self, user):
        income_ledgers = Ledger.objects.filter(
            user=user,
            type='수입'
        )

        return income_ledgers

    def get_outcome_ledgers(self, user):
        outcome_ledgers = Ledger.objects.filter(
            user=user,
            type='지출',
        )
        return outcome_ledgers


class Item(models.Model):
    item = models.CharField(max_length=40)

    def __str__(self):
        return self.item


class Ledger(LedgerAbstract):
    TYPE_CHOICES = [
        ('수입', '수입'),
        ('지출', '지출'),
    ]
    PAYMENT_CHOICES = [
        ('신용카드', '신용카드'),
        ('체크카드', '체크카드'),
        ('현금', '현금'),

    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ledgers")


    date = models.DateTimeField()
    type = models.CharField(max_length=4, choices=TYPE_CHOICES, default='수입')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    business = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    correspondent = models.CharField(max_length=50, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment = models.CharField(max_length=4, choices=PAYMENT_CHOICES, default='체')
    description = models.TextField()

    objects = LedgerManager()

    def __str__(self):
        return f"{self.type} -{self.item}"

    def get_absolute_url(self):
        return reverse("ledgerapp:ledger-detail", args=(self.id,))

    def get_absolute_url2(self):
        return reverse("ledgerapp:dashboard")

    @property
    def get_html_url(self):
        url = reverse("ledgerapp:ledger-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
