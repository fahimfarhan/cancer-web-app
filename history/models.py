from django.db import models

# Create your models here.
from patientbasicinfo.models import Identity


class HistoryModel(models.Model):
    identity_fk = models.ForeignKey(Identity, on_delete=models.CASCADE)
    details = models.CharField(max_length=200, blank=True)
    notes = models.CharField(max_length=200, blank=True)


class HistoryModelFile(models.Model):
    identity_fk = models.ForeignKey(Identity, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/history_file/%Y/%m/%d/%H/%M/%S/')
    fnum = models.IntegerField(default=0)
    name = models.CharField(max_length=100, default='name unavailable')
