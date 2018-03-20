from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from patientbasicinfo.controller import autocomplete
from patientbasicinfo.models import TreatmentPlan
from targetedtherapy.forms import ImmunotherapyForm, TkiForm
from targetedtherapy.models import Immunotherapy, Tki


@login_required
def new_immunotherapy(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if request.method == "POST":
        form = ImmunotherapyForm(request.POST)
        if form.is_valid():
            p_immunotherapy = form.save(commit=False)
            p_immunotherapy.tp_fk = tp_fk
            p_immunotherapy.save()
        return redirect('pbi:view_treatmentplan', p_id, tp_num)
    else:
        form = ImmunotherapyForm()
    ac = autocomplete()
    z = {'form': form, 'type':'Immuno-Therapy'}
    context = {**z, **ac}
    return render(request, 'targetedtherapy/EditTargetedTherapy.html', context)

@login_required
def edit_immunotherapy(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if not Immunotherapy.objects.filter(tp_fk=tp_fk).exists():
        return new_immunotherapy(request, p_id, tp_num)
    else:
        p_targetedtherapy = get_object_or_404(Immunotherapy, tp_fk=tp_fk)
        if request.method == "POST":
            form = ImmunotherapyForm(request.POST, instance=p_targetedtherapy)
            if form.is_valid():
                p_targetedtherapy = form.save()
                return redirect('pbi:view_treatmentplan', p_id, tp_num)
        else:
            form = ImmunotherapyForm(instance=p_targetedtherapy)
        ac = autocomplete()
        z = {'form': form, 'p_targetedtherapy': p_targetedtherapy, 'type':'Immuno-Therapy'}
        context = {**z, **ac}
        return render(request, 'targetedtherapy/EditTargetedTherapy.html', context)



@login_required
def new_tki(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if request.method == "POST":
        form = TkiForm(request.POST)
        if form.is_valid():
            p_tki = form.save(commit=False)
            p_tki.tp_fk = tp_fk
            p_tki.save()
        return redirect('pbi:view_treatmentplan', p_id, tp_num)
    else:
        form = TkiForm()
    ac = autocomplete()
    z = {'form': form, 'type':'TKI'}
    context = {**z, **ac}
    return render(request, 'targetedtherapy/EditTargetedTherapy.html', context)


@login_required
def edit_tki(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if not Tki.objects.filter(tp_fk=tp_fk).exists():
        return new_tki(request, p_id, tp_num)
    else:
        p_targetedtherapy = get_object_or_404(Tki, tp_fk=tp_fk)
        if request.method == "POST":
            form = TkiForm(request.POST, instance=p_targetedtherapy)
            if form.is_valid():
                p_targetedtherapy = form.save()
                return redirect('pbi:view_treatmentplan', p_id, tp_num)
        else:
            form = TkiForm(instance=p_targetedtherapy)
        ac = autocomplete()
        z = {'form': form, 'p_targetedtherapy': p_targetedtherapy, 'type':'TKI'}
        context = {**z, **ac}
        return render(request, 'targetedtherapy/EditTargetedTherapy.html', context)
