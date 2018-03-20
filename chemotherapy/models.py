from django.db import models

# Create your models here.
from patientbasicinfo.models import TreatmentPlan


class ChemoTherapy(models.Model):
    tp_fk = models.ForeignKey(TreatmentPlan, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    details = models.CharField(max_length=200, blank=True)

