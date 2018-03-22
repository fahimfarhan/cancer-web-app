from django.db import models

# Create your models here.
from patientbasicinfo.models import Identity


class Status(models.Model):
    identity_fk = models.OneToOneField(Identity, on_delete=models.CASCADE)
    details = models.CharField(max_length=1000, blank=True)
    advice = models.CharField(max_length=1000, blank=True)


class Investigation(models.Model):
    identity_fk = models.ForeignKey(Identity, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    file = models.FileField(upload_to='uploads/pf_file/%Y/%m/%d/%H/%M/%S/')
    fnum = models.IntegerField(default=0)
    name = models.CharField(max_length=100, default='name unavailable')

    def __str__(self):
        return self.type