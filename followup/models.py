from django.db import models
from django.utils.timezone import now

# Create your models here.
from patientbasicinfo.models import Identity


class FollowUp(models.Model):
    identity_fk = models.ForeignKey(Identity, on_delete=models.CASCADE)
    si_no = models.IntegerField(blank=True)
    date = models.DateField(default=now)
    details = models.CharField(max_length=50, blank=True)
