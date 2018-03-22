import os
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
# class Views:
from patientbasicinfo.controller import autocomplete
from patientbasicinfo.forms import IdentityForm, ComorbidityForm, ProfileForm, UploadForm, PrescriptionForm
from django.utils import timezone

from patientbasicinfo.models import Identity, Comorbidity, Profile, TreatmentPlan, Prescription


@login_required
def ok(request):
    return HttpResponse('<h1>ok</h1>')


@login_required
def edit_profile(request, p_id):
    temp_pk = p_id
    if not Profile.objects.filter(identity=p_id).exists():
        return new_profile(request, p_id)
    else:
        p_profile = get_object_or_404(Profile, identity=p_id)
        if request.method == "POST":
            form = ProfileForm(request.POST, instance=p_profile)
            if form.is_valid():
                p_profile = form.save()
                return redirect('view_patientdetails', p_id=temp_pk)
        else:
            form = ProfileForm(instance=p_profile)  # Profile
        context = {'form': form, 'p_profile': p_profile}
        return render(request, 'patientbasicinfo/EditProfile.html', context)
        # return HttpResponse("ep")


@login_required
def new_profile(request, p_id):
    temp_pk = p_id
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            p_profile = form.save(commit=False)
            p_profile.identity = Identity.objects.get(pk=p_id)
            p_profile.save()
            return redirect('view_patientdetails', p_id=temp_pk)
    else:
        form = ProfileForm()
    context = {'form': form}
    return render(request, 'patientbasicinfo/EditProfile.html', context)


@login_required
def new_identity(request):
    if request.method == "POST":
        form = IdentityForm(request.POST)  # , request.FILES
        if form.is_valid():
            p_identity = form.save(commit=False)
            p_identity.dateOfAdmission = timezone.now()
            # p_identity.image = form.cleaned_data['image']
            p_identity.save()
            return redirect('view_patientdetails', p_id=p_identity.pk)
    else:
        form = IdentityForm()
    return render(request, 'patientbasicinfo/EditIdentity.html', {'form': form})


@login_required
def edit_identity(request, p_id):
    identity = get_object_or_404(Identity, pk=p_id)
    if request.method == "POST":
        form = IdentityForm(request.POST, instance=identity)  # request.FILES,
        if form.is_valid():
            identity = form.save(commit=False)
            identity.dateOfAdmission = timezone.now()
            # identity.image = form.cleaned_data['image']
            identity.save()
            return redirect('view_patientdetails', p_id=identity.pk)
    else:
        form = IdentityForm(instance=identity)
        return render(request, 'patientbasicinfo/EditIdentity.html', {'form': form})


@login_required
def new_comorbidity(request, p_id):
    if request.method == "POST":
        form = ComorbidityForm(request.POST)
        print(1)
        if form.is_valid():
            print(2)
            p_comorbidity = form.save(commit=False)
            p_comorbidity.identity = Identity.objects.get(pk=p_id)
            print(3)
            p_comorbidity.save()
            print(4)
            return redirect('view_patientdetails', p_id=p_comorbidity.identity.pk)
    else:
        print(5)
        form = ComorbidityForm()
    context = {'form': form}
    print(6)
    return render(request, 'patientbasicinfo/EditComorbidity.html', context)
    # return HttpResponse("np")


@login_required
def edit_comorbidity(request, p_id):
    if not Comorbidity.objects.filter(identity=p_id).exists():
        print(1)
        return new_comorbidity(request, p_id)
    else:
        print(2)
        p_comorbidity = get_object_or_404(Comorbidity, identity=p_id)
        print(3)
        print(p_comorbidity.hypertension)
        if request.method == "POST":
            print(p_comorbidity.hypertension)
            form = ComorbidityForm(request.POST, instance=p_comorbidity)
            print(5)
            if form.is_valid():
                print(6)
                p_comorbidity = form.save()
                print(7)
                return redirect('view_patientdetails', p_id=p_comorbidity.identity.pk)
        else:
            print(8)
            form = ComorbidityForm(instance=Comorbidity)
            print(9)
        print(10)
        my_list = myarray(p_comorbidity)
        for i in my_list:
            print(i)
        context = {'form': form, 'p_profile': p_comorbidity, 'my_list': my_list}
        print(11)
        return render(request, 'patientbasicinfo/EditComorbidity.html', context)


def myarray(p_comorbidity):
    my_list = []
    if p_comorbidity.hypertension:
        my_list.append(1)
    else:
        my_list.append(0)
    if p_comorbidity.diabetes:
        my_list.append(1)
    else:
        my_list.append(0)
    if p_comorbidity.cardiac:
        my_list.append(1)
    else:
        my_list.append(0)
    if p_comorbidity.liver:
        my_list.append(1)
    else:
        my_list.append(0)
    if p_comorbidity.kedney:
        my_list.append(1)
    else:
        my_list.append(0)
    if p_comorbidity.others:
        my_list.append(1)
    else:
        my_list.append(0)
    return my_list


@login_required
def upload_handler(request, p_id):
    pid = p_id
    identity = get_object_or_404(Identity, pk=p_id)
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES, instance=identity)
        if form.is_valid():
            p_upload = form.save(commit=False)
            p_upload.pk = p_id  # Investigations.
            p_upload.image = form.cleaned_data['image']
            # p_upload.name = form.cleaned_data['file'].name
            p_upload.save()
            return redirect('view_patientdetails', p_id=pid)
    else:
        form = UploadForm(instance=Identity)
    context = {'form': form}
    return render(request, 'uploadfile/uploadfile.html', context)


@login_required
def delete_propic(request, p_id):
    old_file = None
    identity = get_object_or_404(Identity, pk=p_id)
    try:
        old_file = Identity.objects.get(pk=p_id).image
    except:  # Identity.DoesNotExist:
        print("Most probably file doesnot exist!")
        return False
    if os.path.isfile(old_file.path):
        print("dadada")
        os.remove(old_file.path)
        identity.image = None
        identity.save()
    print("xoxoxo")
    return redirect('view_patientdetails', p_id=p_id)


@login_required
def change_propic(request, p_id):
    pid = p_id
    identity = get_object_or_404(Identity, pk=p_id)
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES, instance=identity)
        if form.is_valid():
            old_file = None
            identity = get_object_or_404(Identity, pk=p_id)
            try:
                old_file = Identity.objects.get(pk=p_id).image
            except:  # Identity.DoesNotExist:
                print("Most probably file doesnot exist!")
                return False
            if os.path.isfile(old_file.path):
                print("dadada")
                os.remove(old_file.path)
                identity.image = None
                identity.save()
            print("xoxoxo")
            p_upload = form.save(commit=False)
            p_upload.pk = p_id  # Investigations.
            p_upload.image = form.cleaned_data['image']
            # p_upload.name = form.cleaned_data['file'].name
            p_upload.save()
            return redirect('view_patientdetails', p_id=pid)
    else:
        form = UploadForm(instance=Identity)
    context = {'form': form}
    return render(request, 'uploadfile/uploadfile.html', context)


@login_required
def new_treatmentplan(request, p_id):
    pid = p_id
    number = 1
    try:
        number = 1 + TreatmentPlan.objects.filter(identity_fk=p_id).latest('num').num
    except:  # num = 1 + Investigations.objects.filter(identity_fk=p_id, type=data.type).count()
        print("Exception at upload handler history/views.py")
    identity = get_object_or_404(Identity, pk=p_id)
    tp = TreatmentPlan(identity_fk=identity, num=number)
    tp.save()
    return redirect('pbi:view_treatmentplan', p_id=pid, tp_num=number)


@login_required
def edit_prescription(request, p_id, number):
    pid = p_id
    if not Prescription.objects.filter(identity_fk=p_id, num=number).exists():
        return new_prescription(request, p_id)
    else:
        p_prescription = get_object_or_404(Prescription, identity_fk=p_id, num=number)
        if request.method == "POST":
            form = PrescriptionForm(request.POST, instance=p_prescription)
            if form.is_valid():
                p_investigations = form.save()  # """ ekhane change kora lagte pare"""
                return redirect('view_patientdetails', p_id=pid)
        else:
            form = PrescriptionForm(instance=Prescription)
        ac = autocomplete()
        z = {'form': form, 'p_prescription': p_prescription}
        context = {**z, **ac}
        return render(request, 'patientbasicinfo/EditPrescription.html', context)


@login_required
def new_prescription(request, p_id):
    pid = p_id
    num = 1
    if request.method == "POST":
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.identity_fk = Identity.objects.get(pk=p_id)
            try:
                num = 1 + Prescription.objects.filter(identity_fk=p_id).latest('num').num
            except:
                print("Exception! Shit!")
            data.num = num
            data.date  = timezone.now()
            data.save()
        return redirect('view_patientdetails', p_id=pid)
    else:
        form = PrescriptionForm()
    ac = autocomplete()
    z = {'form': form}
    context = {**z, **ac}
    return render(request, 'patientbasicinfo/EditPrescription.html', context)


@login_required
def delete_prescription(request, p_id, number):
    p = get_object_or_404(Prescription, identity_fk=p_id, num=number)
    p.delete()
    return redirect('view_patientdetails', p_id=p_id)


@login_required
def delete_treatmentplan(request, p_id, number):
    p = get_object_or_404(TreatmentPlan, identity_fk=p_id, num=number)
    p.delete()
    return redirect('view_patientdetails', p_id=p_id)
