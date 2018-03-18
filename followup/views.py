from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from followup.forms import FollowUpForm
from followup.models import FollowUp
# from patientbasicinfo.controller import autocomplete
from patientbasicinfo.models import Identity


@login_required
def new_followup(request, p_id):
    pk1 = p_id
    num = 1 + FollowUp.objects.filter(identity_fk=p_id).count()
    if request.method == "POST":
        form = FollowUpForm(request.POST)
        if form.is_valid():
            p_followup = form.save(commit=False)
            p_followup.identity_fk = Identity.objects.get(pk=p_id)
            p_followup.si_no = num
            p_followup.save()
        return redirect('view_patientdetails', p_id=pk1)
    else:
        form = FollowUpForm()
    context = {'form': form}
    return render(request, 'followup/EditFollowUp.html', context)


@login_required
def edit_followup(request, p_id, si_no):
    pk = p_id
    if not FollowUp.objects.filter(identity_fk=p_id).exists():
        return new_followup(request, p_id)
    else:
        p_followup = get_object_or_404(FollowUp, identity_fk=p_id, si_no=si_no)
        if request.method == "POST":
            form = FollowUpForm(request.POST, instance=p_followup)
            if form.is_valid():
                p_followup = form.save()
                return redirect('view_patientdetails', p_id=pk)
        else:
            form = FollowUpForm(instance=p_followup)
        # ac = autocomplete()
        context = {'form': form, 'p_followup':p_followup}
        # context = {**z, **ac}
        return render(request, 'followup/EditFollowUp.html', context)

