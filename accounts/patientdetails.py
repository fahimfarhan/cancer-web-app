from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, get_list_or_404

from followup.models import FollowUp
from history.models import HistoryModel, HistoryModelFile
from patientbasicinfo.models import Identity, Comorbidity, Profile, TreatmentPlan
from presentingfeatures.models import Status, Investigation
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
    if not Status.objects.filter(identity_fk=p_id).exists():
        status = None
    else:
        status = get_object_or_404(Status, identity_fk=p_id)
    if not Investigation.objects.filter(identity_fk=p_id, type='Marker').exists():
        markerfile = None
    else:
        markerfile = get_list_or_404(Investigation, identity_fk=p_id, type='Marker')
    if not Investigation.objects.filter(identity_fk=p_id, type='X-ray').exists():
        xrayfile = None
    else:
        xrayfile = get_list_or_404(Investigation, identity_fk=p_id, type='X-ray')
    if not Investigation.objects.filter(identity_fk=p_id, type='USG').exists():
        usgfile = None
    else:
        usgfile = get_list_or_404(Investigation, identity_fk=p_id, type='USG')
    if not Investigation.objects.filter(identity_fk=p_id, type='CT-Scan').exists():
        ctscanfile = None
    else:
        ctscanfile = get_list_or_404(Investigation, identity_fk=p_id, type='CT-Scan')
    if not Investigation.objects.filter(identity_fk=p_id, type='MRI').exists():
        mrifile = None
    else:
        mrifile = get_list_or_404(Investigation, identity_fk=p_id, type='MRI')
    if not Investigation.objects.filter(identity_fk=p_id, type='MRS').exists():
        mrsfile = None
    else:
        mrsfile = get_list_or_404(Investigation, identity_fk=p_id, type='MRS')
    if not Investigation.objects.filter(identity_fk=p_id, type='PET').exists():
        petfile = None
    else:
        petfile = get_list_or_404(Investigation, identity_fk=p_id, type='PET')
    if not Investigation.objects.filter(identity_fk=p_id, type='Echo').exists():
        echofile = None
    else:
        echofile = get_list_or_404(Investigation, identity_fk=p_id, type='Echo')
    if not Investigation.objects.filter(identity_fk=p_id, type='CBC').exists():
        cbcfile = None
    else:
        cbcfile = get_list_or_404(Investigation, identity_fk=p_id, type='CBC')
    if not Investigation.objects.filter(identity_fk=p_id, type='RBS').exists():
        rbsfile = None
    else:
        rbsfile = get_list_or_404(Investigation, identity_fk=p_id, type='RBS')
    if not Investigation.objects.filter(identity_fk=p_id, type='LFT').exists():
        lftfile = None
    else:
        lftfile = get_list_or_404(Investigation, identity_fk=p_id, type='LFT')
    if not Investigation.objects.filter(identity_fk=p_id, type='KFT').exists():
        kftfile = None
    else:
        kftfile = get_list_or_404(Investigation, identity_fk=p_id, type='KFT')
    if not Investigation.objects.filter(identity_fk=p_id, type='Serum-Electrolytes').exists():
        sefile = None
    else:
        sefile = get_list_or_404(Investigation, identity_fk=p_id, type='Serum-Electrolytes')
    if not Investigation.objects.filter(identity_fk=p_id, type='Others').exists():
        ofile = None
    else:
        ofile = get_list_or_404(Investigation, identity_fk=p_id, type='Others')
    ###############################################################################################3
    if not TreatmentPlan.objects.filter(identity_fk=p_id).exists():
        treatmentplan = None
    else:
        treatmentplan = get_list_or_404(TreatmentPlan, identity_fk=p_id)

    context = {'patient': patient, 'comorbidity': comorbidity, 'profile': profile, 'followup': followup,
               'referralnote': referralnote, 'history': history, 'historyfile': historyfile, 'status': status,
               'markerfile': markerfile,'xrayfile': xrayfile, 'usgfile':usgfile, 'ctscanfile':ctscanfile,
               'mrifile':mrifile,'mrsfile':mrsfile, 'petfile':petfile, 'echofile':echofile, 'cbcfile':cbcfile,
               'rbsfile':rbsfile, 'lftfile':lftfile, 'kftfile':kftfile, 'sefile':sefile, 'ofile':ofile,
               'treatmentplan':treatmentplan}
    return render(request, 'accounts/patientdetails.html', context)
