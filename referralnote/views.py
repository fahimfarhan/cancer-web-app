from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
# from patientbasicinfo.controller import autocomplete
from patientbasicinfo.models import Identity
from referralnote.forms import ReferralNoteForm
from referralnote.models import ReferralNote


# class ReferralNotes:
@login_required
def delete_refnote(request, p_id, notenum):
    if not ReferralNote.objects.filter(identity=p_id).exists():
        raise Http404
    else:
        p = get_object_or_404(ReferralNote, identity=p_id, noteNo=notenum)
    p.delete()
    return redirect('view_patientdetails', p_id=p.identity.pk)


@login_required
def edit_referralnote(request, p_id, notenum):
    if not ReferralNote.objects.filter(identity=p_id).exists():
        return new_referralnote(request, p_id)
    else:
        p_referralnote = get_object_or_404(ReferralNote, identity=p_id, noteNo=notenum)
        if request.method == "POST":
            form = ReferralNoteForm(request.POST, instance=p_referralnote)
            if form.is_valid():
                p_referralnote = form.save()
                return redirect('view_patientdetails', p_id=p_referralnote.identity.pk)
        else:
            form = ReferralNoteForm(instance=p_referralnote)
            context = {'form': form, 'p_referralnote': p_referralnote}
        return render(request, 'referralnote/EditReferralNote.html', context)
        # return HttpResponse("Edit referralnote")


@login_required
def new_referralnote(request, p_id):
    num=1
    try:
        num = 1 + ReferralNote.objects.filter(identity=p_id).latest('noteNo').noteNo
    except:  # num = 1 + Investigations.objects.filter(identity_fk=p_id, type=data.type).count()
        print("Exception at upload handler referralnote/ReferralNote.py")
    if request.method == "POST":
        form = ReferralNoteForm(request.POST)
        if form.is_valid():
            p_referralnote = form.save(commit=False)
            p_referralnote.identity = Identity.objects.get(pk=p_id)
            p_referralnote.noteNo = num
            p_referralnote.save()
        return redirect('view_patientdetails', p_id=p_referralnote.identity.pk)
    else:
        form = ReferralNoteForm()
        context = {'form': form}
    return render(request, 'referralnote/EditReferralNote.html', context)
    # return HttpResponse("new referralnote")
