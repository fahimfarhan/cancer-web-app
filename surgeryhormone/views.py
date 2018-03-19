from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from patientbasicinfo.controller import autocomplete
from patientbasicinfo.models import TreatmentPlan
from surgeryhormone.forms import HormoneForm, SurgeryForm
from surgeryhormone.models import Hormone, Surgery


@login_required
def new_surgery(request, p_id, tp_num):
    if request.method == "POST":
        form = SurgeryForm(request.POST)
        if form.is_valid():
            p_surgery = form.save(commit=False)
            tmp_tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
            p_surgery.tp_fk = tmp_tp_fk
            p_surgery.save()
        return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
    else:
        form = HormoneForm()
    ac = autocomplete()
    z = {'form': form}
    context = {**z, **ac}
    return render(request, 'surgeryhormone/EditSurgery.html', context)


@login_required
def edit_surgery(request, p_id,tp_num):
    tp = TreatmentPlan.objects.get(identity_fk = p_id, num=tp_num)
    if not Surgery.objects.filter(tp_fk=tp).exists():
        return new_surgery(request, p_id,tp_num)
    else:
        p_surgery = get_object_or_404(Surgery, tp_fk=tp)
        if request.method == "POST":
            form = SurgeryForm(request.POST, instance=p_surgery)
            if form.is_valid():
                p_surgery = form.save()
                return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
        else:
            form = SurgeryForm(instance=p_surgery)
        ac = autocomplete()
        z = {'form': form, 'p_surgery': p_surgery}
        context = {**z, **ac}
        return render(request, 'surgeryhormone/EditSurgery.html', context)


@login_required
def new_hormone(request, p_id, tp_num):
    if request.method == "POST":
        form = HormoneForm(request.POST)
        if form.is_valid():
            p_hormone = form.save(commit=False)
            tmp_tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
            p_hormone.tp_fk = tmp_tp_fk
            p_hormone.save()
        return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
    else:
        form = HormoneForm()
    ac = autocomplete()
    z = {'form': form}
    context = {**z, **ac}
    return render(request, 'surgeryhormone/EditHormone.html', context)


@login_required
def edit_hormone(request, p_id,tp_num):
    tp = TreatmentPlan.objects.get(identity_fk = p_id, num=tp_num)
    if not Hormone.objects.filter(tp_fk=tp).exists():
        return new_hormone(request, p_id,tp_num)
    else:
        p_hormone = get_object_or_404(Hormone, tp_fk=tp)
        if request.method == "POST":
            form = HormoneForm(request.POST, instance=p_hormone)
            if form.is_valid():
                p_hormone = form.save()
                return redirect('pbi:view_treatmentplan', p_id=p_id, tp_num=tp_num)
        else:
            form = HormoneForm(instance=p_hormone)
        ac = autocomplete()
        z = {'form': form, 'p_hormone': p_hormone}
        context = {**z, **ac}
        return render(request, 'surgeryhormone/EditHormone.html', context)