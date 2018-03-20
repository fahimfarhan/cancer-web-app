from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from patientbasicinfo.models import Identity, TreatmentPlan
from radiotherapy.models import RadioTherapy
from surgeryhormone.models import Hormone, Surgery


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

    context = {'patient': patient, 'tp_fk': tp_fk, 'hormone': hormone, 'surgery': surgery, 'cobalt': cobalt,
               'linac': linac, 'brachy': brachy }
    return render(request, 'treatmentplan/ViewTreatmentPlan.html', context)
