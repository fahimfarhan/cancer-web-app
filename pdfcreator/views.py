import pdfkit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from accounts.models import Doctor
from patientbasicinfo.models import Prescription, Identity, Profile

# Create your views here.


# @login_required
from referralnote.models import ReferralNote


def view_prescription(request, p_id, number, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    doctor = get_object_or_404(Doctor, identity_fk=user)
    profile = get_object_or_404(Profile, identity=p_id)
    prescription = get_object_or_404(Prescription, identity_fk=p_id, num=number)
    context = {'prescription': prescription, 'user': user, 'doctor': doctor, 'profile':profile}
    return render(request, 'pdfcreator/pdfprescription.html', context)


@login_required
def print_prescription(request, p_id, number):
    # Use False instead of output path to save pdf to a variable
    projectUrl = request.get_host() + '/pdfcreator/view/prescription/' + p_id + '/' + number + '/' + str(
        request.user.pk) + '/'  # edit here...
    pdf = pdfkit.from_url(projectUrl, False)
    # Generate download
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="prescription.pdf"'

    return response


def view_referralnote(request, p_id, number, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    doctor = get_object_or_404(Doctor, identity_fk=user)
    # identity = get_object_or_404(Identity, pk=p_id)
    profile = get_object_or_404(Profile, identity=p_id)
    referralnote = get_object_or_404(ReferralNote, identity=p_id, noteNo=number)
    context = {'referralnote': referralnote, 'user': user, 'doctor': doctor, 'profile':profile}
    return render(request, 'pdfcreator/pdfreferralnote.html', context)


@login_required
def print_referralnote(request, p_id, number):
    # Use False instead of output path to save pdf to a variable
    projectUrl = request.get_host() + '/pdfcreator/view/referralnote/' + p_id + '/' + number + '/' + str(
        request.user.pk) + '/'  # edit here...
    pdf = pdfkit.from_url(projectUrl, False)
    # Generate download
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="referralnote.pdf"'

    return response
