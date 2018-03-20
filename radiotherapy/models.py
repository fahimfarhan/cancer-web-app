from django.db import models
# Create your models here.
from django.utils.timezone import now

from patientbasicinfo.models import TreatmentPlan


class RadioTherapy(models.Model):
    tp_fk = models.ForeignKey(TreatmentPlan, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, db_index=True)
    intensity = models.CharField(max_length=50, blank=True)
    dose = models.CharField(max_length=50, blank=True)
    gray = models.FloatField(default=0, blank=True)
    fractionFx = models.FloatField(default=0, blank=True)
    startDate = models.DateField(default=now, blank=True)
    endDate = models.DateField(default=now, blank=True)
    #details = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.identity.name+' - '+self.type
