from django.contrib import admin
from ledgerapp import models


@admin.register(models.Ledger)
class LedgerAdmin(admin.ModelAdmin):
    model = models.Ledger
    list_display = [
        "date", "type", "item", "business", "category", "correspondent", "amount", "payment", "description", "id"
    ]
    search_fields = ["title"]

admin.site.register(models.Item)


# @admin.register(models.EventMember)
# class EventMemberAdmin(admin.ModelAdmin):
#     model = models.EventMember
#     list_display = ["id", "event", "user", "created_at", "updated_at"]
#     list_filter = ["event"]

#["date","type","item","business","category","correspondent","amount","payment","description"]
