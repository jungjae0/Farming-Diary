from django.db import models

# Create your models here.


class Information(models.Model):
    stnId = models.IntegerField()
    stnNm = models.CharField(max_length=20)
    date = models.CharField(max_length=50)
    tavg = models.CharField(max_length=50)
    thum = models.CharField(max_length=50)
    rainfall = models.CharField(max_length=50)
    insolation = models.CharField(max_length=50)

    class Meta:
        db_table = 'weather'