from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from patientbasicinfo.controller import autocomplete
from patientbasicinfo.models import TreatmentPlan
from radiotherapy.forms import RadioTherapyForm


@login_required
def new_Cobalt(request, p_id, tp_num):
    if request.method == "POST":
        form = RadioTherapyForm(request.POST)
        if form.is_valid():
            cobalt = form.save(commit=False)
            tmp_tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
            cobalt.tp_fk = tmp_tp_fk
            cobalt.type = "Cobalt"
            cobalt.save()
        return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
    else:
        form = RadioTherapyForm()
    ac = autocomplete()
    z = {'form': form, 'type': 'Cobalt'}
    context = {**z, **ac}
    return render(request, 'radiotherapy/EditRadioTherapy.html', context)
