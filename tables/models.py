from django.db import models

# Create your models here.
from chemotherapy.models import ChemoTherapy
from radiotherapy.models import RadioTherapy


class Cycle(models.Model):
    cycle = models.IntegerField(blank=True)
    date = models.CharField(max_length=50, blank=True)
    day1 = models.CharField(max_length=50, blank=True)
    day2 = models.CharField(max_length=50, blank=True)
    day3 = models.CharField(max_length=50, blank=True)
    day4 = models.CharField(max_length=50, blank=True)
    day5 = models.CharField(max_length=50, blank=True)
    day8 = models.CharField(max_length=50, blank=True)
    day15 = models.CharField(max_length=50, blank=True)


class NactCycle(Cycle):
    nact_fk = models.ForeignKey(ChemoTherapy, on_delete=models.CASCADE)


class ActCycle(Cycle):
    act_fk = models.ForeignKey(ChemoTherapy, on_delete=models.CASCADE)


class ConcurrentCycle(Cycle):
    concurr_fk = models.ForeignKey(ChemoTherapy, on_delete=models.CASCADE)


class PalliativeCycle(Cycle):
    palliative_fk = models.ForeignKey(ChemoTherapy, on_delete=models.CASCADE)


class RadioTherapyChart(models.Model):
    serialno = models.IntegerField()
    date = models.CharField(max_length=50, blank=True)
    nameoffield = models.CharField(max_length=50, blank=True)
    fieldsize = models.FloatField(blank=True)
    tumordose = models.CharField(max_length=50, blank=True)
    seperation = models.CharField(max_length=50, blank=True)


class CobaltChart(RadioTherapyChart):
    cobalt_fk = models.ForeignKey(RadioTherapy, on_delete=models.CASCADE)


class LinacChart(RadioTherapyChart):
    linac_fk = models.ForeignKey(RadioTherapy, on_delete=models.CASCADE)


class BrachyChart(RadioTherapyChart):
    brachy_fk = models.ForeignKey(RadioTherapy, on_delete=models.CASCADE)


class DiseaseCode(models.Model):
    code = models.CharField(max_length=10)
    meaning = models.CharField(max_length=200)

    def __str__(self):
        return self.code
