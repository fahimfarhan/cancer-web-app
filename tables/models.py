from django.db import models

# Create your models here.
from chemotherapy.models import ChemoTherapy


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


#class RadioTherapyChart(models.Model):
#    date = models.CharField