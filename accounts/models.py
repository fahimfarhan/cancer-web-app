from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Doctor(models.Model):
    identity_fk = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.IntegerField()
    designation = models.CharField(max_length=50, blank=True)
    hospital = models.CharField(max_length=100, blank=True)
