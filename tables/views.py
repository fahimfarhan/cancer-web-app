from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from chemotherapy.models import ChemoTherapy
from patientbasicinfo.models import TreatmentPlan
from tables.forms import NactCycleForm, ActCycleForm, ConcurrentCycleForm, PalliativeCycleForm
from tables.models import NactCycle, ActCycle, ConcurrentCycle, PalliativeCycle


@login_required
def new_nactcycle(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    nact_fk = ChemoTherapy.objects.get(tp_fk=tp_fk, type='NACT')
    num=0
    print(1)
    # num = 1 + CobaltCycle.objects.filter(cobalt_fk=p_id, type="Cobalt").count()
    num = 1 + NactCycle.objects.filter(nact_fk=nact_fk).count()
    print(2)
    if request.method == "POST":
        form = NactCycleForm(request.POST)
        print(3)
        if form.is_valid():
            print(4)
            t_cycle = form.save(commit=False)
            t_cycle.nact_fk = nact_fk
            t_cycle.cycle = num
            t_cycle.save()
            print(5)
        return redirect('pbi:view_treatmentplan', p_id, tp_num)
    else:
        form = NactCycleForm()
        print(6)
    context = {'form': form,'type':'NACT'}
    print(7)
    return render(request, 'tables/EditChemoCycle.html', context)


@login_required
def edit_nactcycle(request, p_id, tp_num, cycleno):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    nact_fk = ChemoTherapy.objects.get(tp_fk=tp_fk, type='NACT')
    num = 0
    if not NactCycle.objects.filter(nact_fk=nact_fk).exists():
        return new_nactcycle(request, p_id, tp_num)
    else:
        t_cycle = get_object_or_404(NactCycle, nact_fk=nact_fk, cycle=cycleno)
        if request.method == "POST":
            form = NactCycleForm(request.POST, instance=t_cycle)
            if form.is_valid():
                t_cycle = form.save()
                return redirect('pbi:view_treatmentplan', p_id, tp_num)
        else:
            form = NactCycleForm(instance=t_cycle)  # NactCycle
        context = {'form': form, 't_cycle': t_cycle, 'type':'NACT'}
        return render(request, 'tables/EditChemoCycle.html', context)

# -----------------------------------------------------------------------------
@login_required
def new_actcycle(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    act_fk = ChemoTherapy.objects.get(tp_fk=tp_fk, type='ACT')
    num=0
    print(1)
    # num = 1 + CobaltCycle.objects.filter(cobalt_fk=p_id, type="Cobalt").count()
    num = 1 + ActCycle.objects.filter(act_fk=act_fk).count()
    print(2)
    if request.method == "POST":
        form = ActCycleForm(request.POST)
        print(3)
        if form.is_valid():
            print(4)
            t_cycle = form.save(commit=False)
            t_cycle.act_fk = act_fk
            t_cycle.cycle = num
            t_cycle.save()
            print(5)
        return redirect('pbi:view_treatmentplan', p_id, tp_num)
    else:
        form = ActCycleForm()
        print(6)
    context = {'form': form, 'type':'ACT'}
    print(7)
    return render(request, 'tables/EditChemoCycle.html', context)


@login_required
def edit_actcycle(request, p_id, tp_num, cycleno):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    act_fk = ChemoTherapy.objects.get(tp_fk=tp_fk, type='ACT')
    num = 0
    if not ActCycle.objects.filter(act_fk=act_fk).exists():
        return new_actcycle(request, p_id, tp_num)
    else:
        t_cycle = get_object_or_404(ActCycle, act_fk=act_fk, cycle=cycleno)
        if request.method == "POST":
            form = ActCycleForm(request.POST, instance=t_cycle)
            if form.is_valid():
                t_cycle = form.save()
                return redirect('pbi:view_treatmentplan', p_id, tp_num)
        else:
            form = ActCycleForm(instance=t_cycle)  # NactCycle
        context = {'form': form, 't_cycle': t_cycle, 'type':'ACT'}
        return render(request, 'tables/EditChemoCycle.html', context)


# ----------------------------------------------------------------------------
@login_required
def new_concurrcycle(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    concurr_fk = ChemoTherapy.objects.get(tp_fk=tp_fk, type='Concurrent')
    num=0
    print(1)
    # num = 1 + CobaltCycle.objects.filter(cobalt_fk=p_id, type="Cobalt").count()
    num = 1 + ConcurrentCycle.objects.filter(concurr_fk=concurr_fk).count()
    print(2)
    if request.method == "POST":
        form = ConcurrentCycleForm(request.POST)
        print(3)
        if form.is_valid():
            print(4)
            t_cycle = form.save(commit=False)
            t_cycle.concurr_fk = concurr_fk
            t_cycle.cycle = num
            t_cycle.save()
            print(5)
        return redirect('pbi:view_treatmentplan', p_id, tp_num)
    else:
        form = ConcurrentCycleForm()
        print(6)
    context = {'form': form, 'type':'Concurrent'}
    print(7)
    return render(request, 'tables/EditChemoCycle.html', context)


@login_required
def edit_concurrcycle(request, p_id, tp_num, cycleno):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    concurr_fk = ChemoTherapy.objects.get(tp_fk=tp_fk, type='Concurrent')
    num = 0
    if not ConcurrentCycle.objects.filter(concurr_fk=concurr_fk).exists():
        return new_concurrcycle(request, p_id, tp_num)
    else:
        t_cycle = get_object_or_404(ConcurrentCycle, concurr_fk=concurr_fk, cycle=cycleno)
        if request.method == "POST":
            form = ConcurrentCycleForm(request.POST, instance=t_cycle)
            if form.is_valid():
                t_cycle = form.save()
                return redirect('pbi:view_treatmentplan', p_id, tp_num)
        else:
            form = ConcurrentCycleForm(instance=t_cycle)  # NactCycle
        context = {'form': form, 't_cycle': t_cycle, 'type':'Concurrent'}
        return render(request, 'tables/EditChemoCycle.html', context)


# ----------------------------------------------------------------------------
@login_required
def new_palliativecycle(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    palliative_fk = ChemoTherapy.objects.get(tp_fk=tp_fk, type='Palliative')
    num=0
    print(1)
    # num = 1 + CobaltCycle.objects.filter(cobalt_fk=p_id, type="Cobalt").count()
    num = 1 + PalliativeCycle.objects.filter(palliative_fk=palliative_fk).count()
    print(2)
    if request.method == "POST":
        form = PalliativeCycleForm(request.POST)
        print(3)
        if form.is_valid():
            print(4)
            t_cycle = form.save(commit=False)
            t_cycle.palliative_fk = palliative_fk
            t_cycle.cycle = num
            t_cycle.save()
            print(5)
        return redirect('pbi:view_treatmentplan', p_id, tp_num)
    else:
        form = PalliativeCycleForm()
        print(6)
    context = {'form': form, 'type':'Palliative'}
    print(7)
    return render(request, 'tables/EditChemoCycle.html', context)


@login_required
def edit_palliativecycle(request, p_id, tp_num, cycleno):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    palliative_fk = ChemoTherapy.objects.get(tp_fk=tp_fk, type='Palliative')
    num = 0
    if not PalliativeCycle.objects.filter(palliative_fk=palliative_fk).exists():
        return new_palliativecycle(request, p_id, tp_num)
    else:
        t_cycle = get_object_or_404(PalliativeCycle, palliative_fk=palliative_fk, cycle=cycleno)
        if request.method == "POST":
            form = PalliativeCycleForm(request.POST, instance=t_cycle)
            if form.is_valid():
                t_cycle = form.save()
                return redirect('pbi:view_treatmentplan', p_id, tp_num)
        else:
            form = PalliativeCycleForm(instance=t_cycle)  # NactCycle
        context = {'form': form, 't_cycle': t_cycle, 'type':'Palliative'}
        return render(request, 'tables/EditChemoCycle.html', context)
