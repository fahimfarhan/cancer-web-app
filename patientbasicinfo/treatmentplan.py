from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from chemotherapy.models import ChemoTherapy
from patientbasicinfo.models import Identity, TreatmentPlan
from radiotherapy.models import RadioTherapy
from surgeryhormone.models import Hormone, Surgery
from targetedtherapy.models import Immunotherapy, Tki


@login_required
def view_treatmentplan(request, p_id, tp_num):
    patient = get_object_or_404(Identity, pk=p_id)
    if not TreatmentPlan.objects.filter(identity_fk=p_id, num=tp_num).exists():
        tp_fk = None
    else:
        tp_fk = get_object_or_404(TreatmentPlan, identity_fk=p_id, num=tp_num)
    if not Hormone.objects.filter(tp_fk=tp_fk).exists():
        hormone = None
    else:
        hormone = get_object_or_404(Hormone, tp_fk=tp_fk)
    if not Surgery.objects.filter(tp_fk=tp_fk).exists():
        surgery = None
    else:
        surgery = get_object_or_404(Surgery, tp_fk=tp_fk)
    if not RadioTherapy.objects.filter(tp_fk=tp_fk, type="Cobalt").exists():
        cobalt = None
    else:
        cobalt = get_object_or_404(RadioTherapy, tp_fk=tp_fk, type="Cobalt")
    if not RadioTherapy.objects.filter(tp_fk=tp_fk, type="Linac").exists():
        linac = None
    else:
        linac = get_object_or_404(RadioTherapy, tp_fk=tp_fk, type="Linac")
    if not RadioTherapy.objects.filter(tp_fk=tp_fk, type="Brachy").exists():
        brachy = None
    else:
        brachy = get_object_or_404(RadioTherapy, tp_fk=tp_fk, type="Brachy")
    if not ChemoTherapy.objects.filter(tp_fk=tp_fk, type="Palliative").exists():
        palliative = None
    else:
        palliative = get_object_or_404(ChemoTherapy, tp_fk=tp_fk, type="Palliative")
    if not ChemoTherapy.objects.filter(tp_fk=tp_fk, type="NACT").exists():
        nact = None
    else:
        nact = get_object_or_404(ChemoTherapy, tp_fk=tp_fk, type="NACT")
    if not ChemoTherapy.objects.filter(tp_fk=tp_fk, type="ACT").exists():
        act = None
    else:
        act = get_object_or_404(ChemoTherapy, tp_fk=tp_fk, type="ACT")
    if not ChemoTherapy.objects.filter(tp_fk=tp_fk, type="Concurrent").exists():
        concurrent = None
    else:
        concurrent = get_object_or_404(ChemoTherapy, tp_fk=tp_fk, type="Concurrent")
    if not Immunotherapy.objects.filter(tp_fk=tp_fk).exists():
        immunotherapy = None
    else:
        immunotherapy = get_object_or_404(Immunotherapy, tp_fk=tp_fk)
    if not Tki.objects.filter(tp_fk=tp_fk).exists():
        tki = None
    else:
        tki = get_object_or_404(Tki, tp_fk=tp_fk)

    context = {'patient': patient, 'tp_fk': tp_fk, 'hormone': hormone, 'surgery': surgery, 'cobalt': cobalt,
               'linac': linac, 'brachy': brachy, 'palliative': palliative, 'nact': nact, 'act': act,
               'concurrent':concurrent, 'immunotherapy':immunotherapy, 'tki': tki}
    return render(request, 'treatmentplan/ViewTreatmentPlan.html', context)
