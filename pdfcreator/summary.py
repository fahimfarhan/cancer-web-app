import pdfkit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, get_list_or_404

from accounts.models import Doctor
from chemotherapy.models import ChemoTherapy
from history.models import HistoryModel
from patientbasicinfo.models import Profile, Identity, Comorbidity, Prescription, TreatmentPlan
from presentingfeatures.models import Status
from radiotherapy.models import RadioTherapy
from referralnote.models import ReferralNote
import datetime

from surgeryhormone.models import Surgery, Hormone
from targetedtherapy.models import Tki, Immunotherapy


def view_report(request, user_pk, p_id, tp_num):
    user = get_object_or_404(User, pk=user_pk)
    now = datetime.datetime.now()
    patient = get_object_or_404(Identity, pk=p_id)
    if not Doctor.objects.filter(identity_fk=user).exists():
        doctor = None
    else:
        doctor = get_object_or_404(Doctor, identity_fk=user)
    tp = get_object_or_404(TreatmentPlan, identity_fk=p_id, num=tp_num)
    if not Surgery.objects.filter(tp_fk=tp).exists():
        surgery = None
    else:
        surgery = get_object_or_404(Surgery, tp_fk=tp)
    if not Hormone.objects.filter(tp_fk=tp).exists():
        hormone = None
    else:
        hormone = get_object_or_404(Hormone, tp_fk=tp)
    if not RadioTherapy.objects.filter(tp_fk=tp, type='Cobalt').exists():
        cobalt = None
    else:
        cobalt = get_object_or_404(RadioTherapy, tp_fk=tp, type='Cobalt')
    if not RadioTherapy.objects.filter(tp_fk=tp, type='Linac').exists():
        linac = None
    else:
        linac = get_object_or_404(RadioTherapy, tp_fk=tp, type='Linac')
    if not RadioTherapy.objects.filter(tp_fk=tp, type='Brachy').exists():
        brachy = None
    else:
        brachy = get_object_or_404(RadioTherapy, tp_fk=tp, type='Brachy')

    if not ChemoTherapy.objects.filter(tp_fk=tp, type='NACT').exists():
        nact = None
    else:
        nact = get_object_or_404(ChemoTherapy, tp_fk=tp, type='NACT')
    if not ChemoTherapy.objects.filter(tp_fk=tp, type='ACT').exists():
        act = None
    else:
        act = get_object_or_404(ChemoTherapy, tp_fk=tp, type='ACT')
    if not ChemoTherapy.objects.filter(tp_fk=tp, type='Palliative').exists():
        palliative = None
    else:
        palliative = get_object_or_404(ChemoTherapy, tp_fk=tp, type='Palliative')
    if not ChemoTherapy.objects.filter(tp_fk=tp, type='Concurrent').exists():
        concurrent = None
    else:
        concurrent = get_object_or_404(ChemoTherapy, tp_fk=tp, type='Concurrent')
    if not Tki.objects.filter(tp_fk=tp).exists():
        tki = None
    else:
        tki = get_object_or_404(Tki, tp_fk=tp)
    if not Immunotherapy.objects.filter(tp_fk=tp).exists():
        immunotherapy = None
    else:
        immunotherapy = get_object_or_404(Tki, tp_fk=tp)
    context = {'user': user, 'doctor': doctor, 'patient': patient, 'now': now, 'surgery': surgery, 'hormone': hormone,
               'cobalt':cobalt, 'linac':linac, 'brachy': brachy,'nact':nact, 'act':act, 'palliative':palliative,
               'concurrent':concurrent,'tki':tki,'immunotherapy':immunotherapy}
    return render(request, 'summary/report.html', context)


@login_required
def print_report(request, p_id, tp_num):
    # Use False instead of output path to save pdf to a variable
    projectUrl = request.get_host() + '/pdfcreator/view/report/' + str(
        request.user.pk) + '/' + p_id + '/' + tp_num + '/'
    # edit here...
    pdf = pdfkit.from_url(projectUrl, False)
    # Generate download
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'

    return response


def view_summary(request, p_id, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    # doctor = get_object_or_404(Doctor, identity_fk=user)
    patient = get_object_or_404(Identity, pk=p_id)
    if not Doctor.objects.filter(identity_fk=user).exists():
        doctor = None
    else:
        doctor = get_object_or_404(Doctor, identity_fk=user)
    if not Comorbidity.objects.filter(identity=p_id).exists():
        comorbidity = None
    else:
        comorbidity = get_object_or_404(Comorbidity, identity=p_id)
    if not Profile.objects.filter(identity=p_id).exists():
        profile = None
    else:
        profile = get_object_or_404(Profile, identity=p_id)
    if not Status.objects.filter(identity_fk=p_id).exists():
        status = None
    else:
        status = get_object_or_404(Status, identity_fk=p_id)
    if not HistoryModel.objects.filter(identity_fk=p_id).exists():
        history = None
    else:
        history = get_object_or_404(HistoryModel, identity_fk=p_id)
    if not Prescription.objects.filter(identity_fk=p_id).exists():
        prescription = None
    else:
        prescription = get_list_or_404(Prescription, identity_fk=p_id)
    if not ReferralNote.objects.filter(identity=p_id).exists():
        referralnote = None
    else:
        referralnote = get_list_or_404(ReferralNote, identity=p_id)

    # referralnote = get_list_or_404(ReferralNote, identity=p_id, noteNo=number)
    context = {'user': user, 'doctor': doctor, 'profile': profile, 'patient': patient, 'comorbidity': comorbidity,
               'status': status, 'history': history, 'prescription': prescription, 'referralnote': referralnote}
    return render(request, 'summary/report.html', context)


@login_required
def print_summary(request, p_id):
    # Use False instead of output path to save pdf to a variable
    projectUrl = request.get_host() + '/pdfcreator/view/summary/' + p_id + '/' + str(
        request.user.pk) + '/'  # edit here...
    pdf = pdfkit.from_url(projectUrl, False)
    # Generate download
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="summary.pdf"'

    return response
