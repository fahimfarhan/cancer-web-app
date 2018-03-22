from chemotherapy.models import ChemoTherapy
from patientbasicinfo.models import Identity, Profile
from radiotherapy.models import RadioTherapy


class QueryController:
    def dosth(self):
        return 1

    # NACT ACT concurrent palliative
    def SelectAllWithNact(self):
        nact = ChemoTherapy.objects.all().filter(type='NACT')
        return nact

    def SelectAllWithAct(self):
        act = ChemoTherapy.objects.all().filter(type='ACT')
        return act

    def SelectAllWithConcurrent(self):
        concurrent = ChemoTherapy.objects.all().filter(type='Concurrent')
        return concurrent

    def SelectAllWithPalliative(self):
        palliative = ChemoTherapy.objects.all().filter(type='Palliative')
        return palliative

    # linac cobalt brachy

    def SelectAllWithCobalt(self):
        cobalt = RadioTherapy.objects.all().filter(type='Cobalt')
        return cobalt


    def SelectAllWithLinac(self):
        linac = RadioTherapy.objects.all().filter(type='Linac')
        return linac

    def SelectAllWithBrachy(self):
        brachy = RadioTherapy.objects.all().filter(type='Brachy')
        return brachy

    def SelectAllWhereUnitIsA(self):
        unit = Identity.objects.all().filter(unit='A')
        return unit

    def SelectAllBetween2Dates(self):
        startdate = '2017-12-5'  # date.today()  #
        enddate = '2017-10-5'  # startdate + timedelta(days=30)  #
        between2dates = Identity.objects.filter(dateOfAdmission__range=[enddate, startdate])
        # Identity.objects.filter(dateOfAdmission=startdate)
        # Identity.objects.filter(dateOfAdmission=[startdate, enddate])
        print(between2dates)
        context = {'between2dates': between2dates}
        return context

    def selectAllWithStage1(self):
        stage_one = Profile.objects.filter(stage=1)
        context = {'stage_one': stage_one}
        return context

    def selectAllWithStage2(self):
        stage_two = Profile.objects.filter(stage=2)
        context = {'stage_two': stage_two}
        return context

    def selectAllWithStage3(self):
        stage_three = Profile.objects.filter(stage=3)
        context = {'stage_three': stage_three}
        return context

    def selectAllWithStage4(self):
        stage_four = Profile.objects.filter(stage=4)
        context = {'stage_four': stage_four}
        return context
