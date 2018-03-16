from django.db import models
from django.utils.timezone import now


# Create your models here.

class Identity(models.Model):
    name = models.CharField(max_length=50)
    mobileNo = models.IntegerField(default=0, db_index=True)
    dateOfAdmission = models.DateField(default=now)
    unit = models.CharField(max_length=5, blank=True)
    religion = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    dateOfBirth = models.DateField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    referredBy = models.CharField(max_length=50, blank=True)
    regNo = models.CharField(max_length=6, blank=True)
    image = models.ImageField(upload_to='uploads/profile_pic/%Y/%m/%d/%H/%M/%S/', blank=True)

    def __str__(self):
        return self.name


class Comorbidity(models.Model):
    identity = models.ForeignKey(Identity, on_delete=models.CASCADE)
    hypertension = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    cardiac = models.BooleanField(default=False)
    liver = models.BooleanField(default=False)
    kedney = models.BooleanField(default=False)
    others = models.BooleanField(default=False)
    # others = models.CharField(max_length=200)

    def __str__(self):
        return self.identity.name