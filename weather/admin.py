from django.contrib import admin

from .models import Information

class InformationAdmin(admin.ModelAdmin):
    list_display = ['stnId', 'stnNm', 'date', 'tavg',
                    'thum', 'rainfall', 'insolation',]

admin.site.register(Information, InformationAdmin)
