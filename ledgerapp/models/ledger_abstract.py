from django.db import models


class LedgerAbstract(models.Model):
    """ Event abstract model """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
