import pdfkit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, get_list_or_404

from accounts.models import Doctor
from history.models import HistoryModel
from patientbasicinfo.models import Profile, Identity, Comorbidity, Prescription
from presentingfeatures.models import Status
from referralnote.models import ReferralNote


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
               'status': status, 'history':history, 'prescription':prescription, 'referralnote':referralnote}
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
