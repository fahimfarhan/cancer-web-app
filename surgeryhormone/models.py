from django.db import models

# Create your models here.
from patientbasicinfo.models import TreatmentPlan


class Surgery(models.Model):
    tp_fk = models.OneToOneField(TreatmentPlan, on_delete=models.CASCADE)
    details = models.CharField(max_length=200)


class Hormone(models.Model):
    tp_fk = models.OneToOneField(TreatmentPlan, on_delete=models.CASCADE)
    details = models.CharField(max_length=200)
