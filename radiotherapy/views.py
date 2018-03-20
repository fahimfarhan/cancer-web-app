from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from patientbasicinfo.controller import autocomplete
from patientbasicinfo.models import TreatmentPlan
from radiotherapy.forms import RadioTherapyForm
from radiotherapy.models import RadioTherapy


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


@login_required
def edit_Cobalt(request, p_id, tp_num):
    tmp_tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if not RadioTherapy.objects.filter(tp_fk=tmp_tp_fk, type="Cobalt").exists():
        return new_Cobalt(request, p_id, tp_num)
    else:
        p_radiotherapy = get_object_or_404(RadioTherapy, tp_fk=tmp_tp_fk, type="Cobalt")
        if request.method == "POST":
            form = RadioTherapyForm(request.POST, instance=p_radiotherapy)
            if form.is_valid():
                p_radiotherapy = form.save()  # """ ekhane change kora lagte pare"""
                return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
        else:
            form = RadioTherapyForm(instance=p_radiotherapy)
        ac = autocomplete()
        z = {'form': form, 'p_radiotherapy': p_radiotherapy, 'type': 'Cobalt'}
        context = {**z, **ac}
        return render(request, 'radiotherapy/EditRadioTherapy.html', context)


@login_required
def new_Linac(request, p_id, tp_num):
    if request.method == "POST":
        form = RadioTherapyForm(request.POST)
        if form.is_valid():
            linac = form.save(commit=False)
            tmp_tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
            linac.tp_fk = tmp_tp_fk
            linac.type = "Linac"
            linac.save()
        return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
    else:
        form = RadioTherapyForm()
    ac = autocomplete()
    z = {'form': form, 'type': 'Linac'}
    context = {**z, **ac}
    return render(request, 'radiotherapy/EditRadioTherapy.html', context)


@login_required
def edit_Linac(request, p_id, tp_num):
    tmp_tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if not RadioTherapy.objects.filter(tp_fk=tmp_tp_fk, type="Linac").exists():
        return new_Linac(request, p_id, tp_num)
    else:
        p_radiotherapy = get_object_or_404(RadioTherapy, tp_fk=tmp_tp_fk, type="Linac")
        if request.method == "POST":
            form = RadioTherapyForm(request.POST, instance=p_radiotherapy)
            if form.is_valid():
                p_radiotherapy = form.save()  # """ ekhane change kora lagte pare"""
                return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
        else:
            form = RadioTherapyForm(instance=p_radiotherapy)
        ac = autocomplete()
        z = {'form': form, 'p_radiotherapy': p_radiotherapy, 'type': 'Linac'}
        context = {**z, **ac}
        return render(request, 'radiotherapy/EditRadioTherapy.html', context)


@login_required
def new_Brachy(request, p_id, tp_num):
    if request.method == "POST":
        form = RadioTherapyForm(request.POST)
        if form.is_valid():
            brachy = form.save(commit=False)
            tmp_tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
            brachy.tp_fk = tmp_tp_fk
            brachy.type = "Brachy"
            brachy.save()
        return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
    else:
        form = RadioTherapyForm()
    ac = autocomplete()
    z = {'form': form, 'type': 'Brachy'}
    context = {**z, **ac}
    return render(request, 'radiotherapy/EditRadioTherapy.html', context)


@login_required
def edit_Brachy(request, p_id, tp_num):
    tmp_tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if not RadioTherapy.objects.filter(tp_fk=tmp_tp_fk, type="Brachy").exists():
        return new_Brachy(request, p_id, tp_num)
    else:
        p_radiotherapy = get_object_or_404(RadioTherapy, tp_fk=tmp_tp_fk, type="Brachy")
        if request.method == "POST":
            form = RadioTherapyForm(request.POST, instance=p_radiotherapy)
            if form.is_valid():
                p_radiotherapy = form.save()  # """ ekhane change kora lagte pare"""
                return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
        else:
            form = RadioTherapyForm(instance=p_radiotherapy)
        ac = autocomplete()
        z = {'form': form, 'p_radiotherapy': p_radiotherapy, 'type': 'Brachy'}
        context = {**z, **ac}
        return render(request, 'radiotherapy/EditRadioTherapy.html', context)
