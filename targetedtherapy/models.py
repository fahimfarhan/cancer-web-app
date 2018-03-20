from django.db import models

# Create your models here.
from patientbasicinfo.models import TreatmentPlan


class TargetedTherapy(models.Model):
    details = models.CharField(max_length=200, blank=True)


class Immunotherapy(TargetedTherapy):
    tp_fk = models.ForeignKey(TreatmentPlan, on_delete=models.CASCADE, default=None)


class Tki(TargetedTherapy):
    tp_fk = models.ForeignKey(TreatmentPlan, on_delete=models.CASCADE, default=None)
