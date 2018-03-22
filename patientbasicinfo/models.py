from django.db import models
from django.utils.timezone import now


# Create your models here.

class Identity(models.Model):
    name = models.CharField(max_length=50)
    mobileNo = models.IntegerField(default=0, db_index=True)
    dateOfAdmission = models.DateField(default=now)
    email = models.EmailField(db_index=True, blank=True)
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


class Profile(models.Model):
    identity = models.ForeignKey(Identity, on_delete=models.CASCADE)
    diseaseCode = models.CharField(max_length=50, blank=True)
    histopathology = models.CharField(max_length=50, blank=True)
    ihc = models.CharField(max_length=50, blank=True)
    er_pr = models.CharField(max_length=50, blank=True)
    stage = models.IntegerField(default=1, blank=True)
    tnm = models.CharField(max_length=50, blank=True)
    height = models.FloatField(max_length=5, blank=True)
    weight = models.FloatField(max_length=5, blank=True)
    bsa = models.FloatField(max_length=10, default=0, blank=True)  # need to fix  this... FloatField hobe!
    ps = models.CharField(max_length=10, blank=True)
    bloodGroup = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return self.identity.name


class Medicine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Dose(models.Model):
    dose = models.CharField(max_length=50)

    def __str__(self):
        return self.dose


class Timetable(models.Model):
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.time


class Bangla(models.Model):
    bangla = models.CharField(max_length=50)

    def __str__(self):
        return self.bangla


class TreatmentPlan(models.Model):
    identity_fk = models.ForeignKey(Identity, on_delete=models.CASCADE)
    num = models.IntegerField()

    def __str__(self):
        return self.identity_fk.name+' '+str(self.num)


class Prescription(models.Model):
    identity_fk = models.ForeignKey(Identity, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    num = models.IntegerField()
    details = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.identity_fk.name + ' ' + str(self.num)
