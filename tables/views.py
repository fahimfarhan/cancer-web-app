from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from chemotherapy.models import ChemoTherapy
from patientbasicinfo.models import TreatmentPlan
from radiotherapy.models import RadioTherapy
from tables.forms import NactCycleForm, ActCycleForm, ConcurrentCycleForm, PalliativeCycleForm, CobaltChartForm, \
    LinacChartForm, BrachyChartForm
from tables.models import NactCycle, ActCycle, ConcurrentCycle, PalliativeCycle, CobaltChart, LinacChart, BrachyChart


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


# --------------------------------RadioTherapy---------------------------------------------
@login_required
def new_cobaltcycle(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    cobalt_fk = RadioTherapy.objects.get(tp_fk=tp_fk, type='Cobalt')
    num=0
    print(1)
    # num = 1 + CobaltCycle.objects.filter(cobalt_fk=p_id, type="Cobalt").count()
    num = 1 + CobaltChart.objects.filter(cobalt_fk=cobalt_fk).count()
    print(2)
    if request.method == "POST":
        form = CobaltChartForm(request.POST)
        print(3)
        if form.is_valid():
            print(4)
            t_cycle = form.save(commit=False)
            t_cycle.cobalt_fk = cobalt_fk
            t_cycle.serialno = num
            t_cycle.save()
            print(5)
        return redirect('pbi:view_treatmentplan', p_id, tp_num)
    else:
        form = CobaltChartForm()
        print(6)
    context = {'form': form, 'type':'Cobalt'}
    print(7)
    return render(request, 'tables/EditRadioCycle.html', context)


@login_required
def edit_cobaltcycle(request, p_id, tp_num, sino):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    cobalt_fk = RadioTherapy.objects.get(tp_fk=tp_fk, type='Cobalt')
    num = 0
    if not CobaltChart.objects.filter(cobalt_fk=cobalt_fk).exists():
        return new_cobaltcycle(request, p_id, tp_num)
    else:
        t_cycle = get_object_or_404(CobaltChart, cobalt_fk=cobalt_fk, serialno=sino)
        if request.method == "POST":
            form = CobaltChartForm(request.POST, instance=t_cycle)
            if form.is_valid():
                t_cycle = form.save()
                return redirect('pbi:view_treatmentplan', p_id, tp_num)
        else:
            form = CobaltChartForm(instance=t_cycle)  # NactCycle
        context = {'form': form, 't_cycle': t_cycle, 'type':'Cobalt'}
        return render(request, 'tables/EditRadioCycle.html', context)


# -----------------------------------------------------------------------------

@login_required
def new_linaccycle(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    linac_fk = RadioTherapy.objects.get(tp_fk=tp_fk, type='Linac')
    num=0
    print(1)
    # num = 1 + CobaltCycle.objects.filter(cobalt_fk=p_id, type="Cobalt").count()
    num = 1 + LinacChart.objects.filter(linac_fk=linac_fk).count()
    print(2)
    if request.method == "POST":
        form = LinacChartForm(request.POST)
        print(3)
        if form.is_valid():
            print(4)
            t_cycle = form.save(commit=False)
            t_cycle.linac_fk = linac_fk
            t_cycle.serialno = num
            t_cycle.save()
            print(5)
        return redirect('pbi:view_treatmentplan', p_id, tp_num)
    else:
        form = LinacChartForm()
        print(6)
    context = {'form': form, 'type':'Linac'}
    print(7)
    return render(request, 'tables/EditRadioCycle.html', context)


@login_required
def edit_linaccycle(request, p_id, tp_num, sino):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    linac_fk = RadioTherapy.objects.get(tp_fk=tp_fk, type='Linac')
    num = 0
    if not LinacChart.objects.filter(linac_fk=linac_fk).exists():
        return new_linaccycle(request, p_id, tp_num)
    else:
        t_cycle = get_object_or_404(LinacChart, linac_fk=linac_fk, serialno=sino)
        if request.method == "POST":
            form = LinacChartForm(request.POST, instance=t_cycle)
            if form.is_valid():
                t_cycle = form.save()
                return redirect('pbi:view_treatmentplan', p_id, tp_num)
        else:
            form = LinacChartForm(instance=t_cycle)  # NactCycle
        context = {'form': form, 't_cycle': t_cycle, 'type':'Linac'}
        return render(request, 'tables/EditRadioCycle.html', context)


# -----------------------------------------------------------------------------

@login_required
def new_brachycycle(request, p_id, tp_num):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    brachy_fk = RadioTherapy.objects.get(tp_fk=tp_fk, type='Brachy')
    num=0
    print(1)
    # num = 1 + CobaltCycle.objects.filter(cobalt_fk=p_id, type="Cobalt").count()
    num = 1 + BrachyChart.objects.filter(brachy_fk=brachy_fk).count()
    print(2)
    if request.method == "POST":
        form = BrachyChartForm(request.POST)
        print(3)
        if form.is_valid():
            print(4)
            t_cycle = form.save(commit=False)
            t_cycle.brachy_fk = brachy_fk
            t_cycle.serialno = num
            t_cycle.save()
            print(5)
        return redirect('pbi:view_treatmentplan', p_id, tp_num)
    else:
        form = BrachyChartForm()
        print(6)
    context = {'form': form, 'type':'Brachy'}
    print(7)
    return render(request, 'tables/EditRadioCycle.html', context)


@login_required
def edit_brachycycle(request, p_id, tp_num, sino):
    tp_fk = TreatmentPlan.objects.get(identity_fk=p_id, num=tp_num)
    brachy_fk = RadioTherapy.objects.get(tp_fk=tp_fk, type='Brachy')
    num = 0
    if not BrachyChart.objects.filter(brachy_fk=brachy_fk).exists():
        return new_brachycycle(request, p_id, tp_num)
    else:
        t_cycle = get_object_or_404(BrachyChart, brachy_fk=brachy_fk, serialno=sino)
        if request.method == "POST":
            form = BrachyChartForm(request.POST, instance=t_cycle)
            if form.is_valid():
                t_cycle = form.save()
                return redirect('pbi:view_treatmentplan', p_id, tp_num)
        else:
            form = BrachyChartForm(instance=t_cycle)  # NactCycle
        context = {'form': form, 't_cycle': t_cycle, 'type':'Brachy'}
        return render(request, 'tables/EditRadioCycle.html', context)
