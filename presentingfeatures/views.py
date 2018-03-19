import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from filetransfers.api import serve_file
# Create your views here.
from patientbasicinfo.controller import autocomplete
from patientbasicinfo.models import Identity
from presentingfeatures.forms import StatusForm, UploadForm
from presentingfeatures.models import Status, Investigation


@login_required
def new_status(request, p_id):
    pid = p_id
    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            p_status = form.save(commit=False)
            p_status.identity_fk = Identity.objects.get(pk=p_id)
            p_status.save()
        return redirect('view_patientdetails', p_id=pid)
    else:
        form = StatusForm()
    ac = autocomplete()
    z = {'form': form}
    context = {**z, **ac}
    return render(request, 'status/EditStatus.html', context)


@login_required
def edit_status(request, p_id):
    pid = p_id
    if not Status.objects.filter(identity_fk=p_id).exists():
        return new_status(request, p_id)
    else:
        p_status = get_object_or_404(Status, identity_fk=p_id)
        if request.method == "POST":
            form = StatusForm(request.POST, instance=p_status)
            if form.is_valid():
                p_status = form.save()
                return redirect('view_patientdetails', p_id=pid)
        else:
            form = StatusForm(instance=p_status)
        ac = autocomplete()
        z = {'form': form, 'p_status': p_status}
        context = {**z, **ac}
        return render(request, 'status/EditStatus.html', context)


@login_required
def delete_file(request, p_id, ftype, num):
    pid = p_id
    p = get_object_or_404(Investigation, identity_fk=p_id,type=ftype, fnum=num)
    old_file = p.file
    if os.path.isfile(old_file.path):
        print("dadada")
        os.remove(old_file.path)
    p.delete()
    return redirect('view_patientdetails', p_id=pid)


@login_required
def download_file(request, p_id, ftype, num):
    upload = get_object_or_404(Investigation, identity_fk=p_id, type=ftype, fnum=num)
    return serve_file(request, upload.file)


@login_required
def upload_handler(request, p_id):
    pid = p_id
    fnum = 1

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            p_upload = form.save(commit=False)
            p_upload.identity_fk = get_object_or_404(Identity, pk=p_id)  # Investigations.
            p_upload.file = form.cleaned_data['file']
            temp_type = form.cleaned_data['type']
            try:
                fnum = 1 + Investigation.objects.filter(identity_fk=p_id, type=temp_type).latest('fnum').fnum
            except:  # num = 1 + Investigations.objects.filter(identity_fk=p_id, type=data.type).count()
                print("Exception at upload handler presentingfeatures/views.py")
            p_upload.fnum = fnum
            p_upload.name = form.cleaned_data['file'].name
            p_upload.save()
            return redirect('view_patientdetails', p_id=pid)
    else:
        form = UploadForm()
    context = {'form': form}
    return render(request, 'uploadfile/uploadfile.html', context)
