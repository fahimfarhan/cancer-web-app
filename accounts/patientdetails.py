from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, get_list_or_404

from followup.models import FollowUp
from history.models import HistoryModel, HistoryModelFile
from patientbasicinfo.models import Identity, Comorbidity, Profile
from referralnote.models import ReferralNote


@login_required
def view_patientdetails(request, p_id):
    patient = get_object_or_404(Identity, pk=p_id)
    if not Profile.objects.filter(identity=p_id).exists():
        profile = None
    else:
        profile = get_object_or_404(Profile, identity=p_id)

    if not Comorbidity.objects.filter(identity=p_id).exists():
        comorbidity = None
    else:
        comorbidity = get_object_or_404(Comorbidity, identity=p_id)
    if not FollowUp.objects.filter(identity_fk=p_id).exists():
        followup = None
    else:
        followup = get_list_or_404(FollowUp, identity_fk=p_id)
    if not ReferralNote.objects.filter(identity=p_id).exists():
        referralnote = None
    else:
        referralnote = get_list_or_404(ReferralNote, identity=p_id)
    if not HistoryModel.objects.filter(identity_fk=p_id).exists():
        history = None
    else:
        history = get_object_or_404(HistoryModel, identity_fk=p_id)
    if not HistoryModelFile.objects.filter(identity_fk=p_id).exists():
        historyfile = None
    else:
        historyfile = get_list_or_404(HistoryModelFile, identity_fk=p_id)

    context = {'patient': patient, 'comorbidity': comorbidity, 'profile': profile, 'followup': followup,
               'referralnote': referralnote, 'history': history, 'historyfile': historyfile}
    return render(request, 'accounts/patientdetails.html', context)
