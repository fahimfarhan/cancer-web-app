from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from chemotherapy.forms import ChemoTherapyForm
from chemotherapy.models import ChemoTherapy
from patientbasicinfo.controller import autocomplete
from patientbasicinfo.models import TreatmentPlan


@login_required
def new_palliative(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if request.method == "POST":
        form = ChemoTherapyForm(request.POST)
        if form.is_valid():
            palliative = form.save(commit=False)
            palliative.tp_fk = tp_fk
            palliative.type = "Palliative"
            palliative.save()
        return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
    else:
        form = ChemoTherapyForm()
    ac = autocomplete()
    z = {'form': form, 'type': 'Palliative'}
    context = {**z, **ac}
    return render(request, 'chemotherapy/EditChemoTherapy.html', context)


@login_required
def edit_palliative(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if not ChemoTherapy.objects.filter(tp_fk=tp_fk, type="Palliative").exists():
        return new_palliative(request, p_id, tp_num)
    else:
        p_chemotherapy = get_object_or_404(ChemoTherapy, tp_fk=tp_fk, type="Palliative")
        if request.method == "POST":
            form = ChemoTherapyForm(request.POST, instance=p_chemotherapy)
            if form.is_valid():
                p_chemotherapy = form.save()  # """ ekhane change kora lagte pare"""
                return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
        else:
            form = ChemoTherapyForm(instance=p_chemotherapy)
        ac = autocomplete()
        z = {'form': form, 'p_chemotherapy': p_chemotherapy, 'type': 'Palliative'}
        context = {**z, **ac}
        return render(request, 'chemotherapy/EditChemoTherapy.html', context)


@login_required
def new_nact(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if request.method == "POST":
        form = ChemoTherapyForm(request.POST)
        if form.is_valid():
            nact = form.save(commit=False)
            nact.tp_fk = tp_fk
            nact.type = "NACT"
            nact.save()
        return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
    else:
        form = ChemoTherapyForm()
    ac = autocomplete()
    z = {'form': form, 'type': 'NACT'}
    context = {**z, **ac}
    return render(request, 'chemotherapy/EditChemoTherapy.html', context)


@login_required
def edit_nact(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if not ChemoTherapy.objects.filter(tp_fk=tp_fk, type="NACT").exists():
        return new_nact(request, p_id, tp_num)
    else:
        p_chemotherapy = get_object_or_404(ChemoTherapy, tp_fk=tp_fk, type="NACT")
        if request.method == "POST":
            form = ChemoTherapyForm(request.POST, instance=p_chemotherapy)
            if form.is_valid():
                p_chemotherapy = form.save()  # """ ekhane change kora lagte pare"""
                return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
        else:
            form = ChemoTherapyForm(instance=p_chemotherapy)
        ac = autocomplete()
        z = {'form': form, 'p_chemotherapy': p_chemotherapy, 'type': 'NACT'}
        context = {**z, **ac}
        return render(request, 'chemotherapy/EditChemoTherapy.html', context)


@login_required
def new_act(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if request.method == "POST":
        form = ChemoTherapyForm(request.POST)
        if form.is_valid():
            act = form.save(commit=False)
            act.tp_fk = tp_fk
            act.type = "ACT"
            act.save()
        return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
    else:
        form = ChemoTherapyForm()
    ac = autocomplete()
    z = {'form': form, 'type': 'ACT'}
    context = {**z, **ac}
    return render(request, 'chemotherapy/EditChemoTherapy.html', context)


@login_required
def edit_act(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if not ChemoTherapy.objects.filter(tp_fk=tp_fk, type="ACT").exists():
        return new_nact(request, p_id, tp_num)
    else:
        p_chemotherapy = get_object_or_404(ChemoTherapy, tp_fk=tp_fk, type="ACT")
        if request.method == "POST":
            form = ChemoTherapyForm(request.POST, instance=p_chemotherapy)
            if form.is_valid():
                p_chemotherapy = form.save()  # """ ekhane change kora lagte pare"""
                return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
        else:
            form = ChemoTherapyForm(instance=p_chemotherapy)
        ac = autocomplete()
        z = {'form': form, 'p_chemotherapy': p_chemotherapy, 'type': 'ACT'}
        context = {**z, **ac}
        return render(request, 'chemotherapy/EditChemoTherapy.html', context)


@login_required
def new_concurrent(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if request.method == "POST":
        form = ChemoTherapyForm(request.POST)
        if form.is_valid():
            concurrent = form.save(commit=False)
            concurrent.tp_fk = tp_fk
            concurrent.type = "Concurrent"
            concurrent.save()
        return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
    else:
        form = ChemoTherapyForm()
    ac = autocomplete()
    z = {'form': form, 'type': 'Concurrent'}
    context = {**z, **ac}
    return render(request, 'chemotherapy/EditChemoTherapy.html', context)


@login_required
def edit_concurrent(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    if not ChemoTherapy.objects.filter(tp_fk=tp_fk, type="Concurrent").exists():
        return new_concurrent(request, p_id, tp_num)
    else:
        p_chemotherapy = get_object_or_404(ChemoTherapy, tp_fk=tp_fk, type="Concurrent")
        if request.method == "POST":
            form = ChemoTherapyForm(request.POST, instance=p_chemotherapy)
            if form.is_valid():
                p_chemotherapy = form.save()  # """ ekhane change kora lagte pare"""
                return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
        else:
            form = ChemoTherapyForm(instance=p_chemotherapy)
        ac = autocomplete()
        z = {'form': form, 'p_chemotherapy': p_chemotherapy, 'type': 'Concurrent'}
        context = {**z, **ac}
        return render(request, 'chemotherapy/EditChemoTherapy.html', context)
