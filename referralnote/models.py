from django.db import models


# Create your models here.
from patientbasicinfo.models import Identity


class ReferralNote(models.Model):
    identity = models.ForeignKey(Identity, on_delete=models.CASCADE)
    purpose =  models.CharField(max_length=500, blank=True)
    condition = models.CharField(max_length=500,blank=True)
    refferedDept = models.CharField(max_length=200,blank=True)
    refferedConsultant = models.CharField(max_length=200,blank=True)
    responseNote = models.CharField(max_length=500,blank=True)
    remarks = models.CharField(max_length=500,blank=True)
    noteNo = models.IntegerField()

    def __str__(self):
        return self.identity.name
