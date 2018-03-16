from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
# class Views:
from patientbasicinfo.forms import IdentityForm
from django.utils import timezone

from patientbasicinfo.models import Identity


@login_required
def ok(request):
    return HttpResponse('<h1>ok</h1>')


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
        form = IdentityForm(request.POST, instance=identity)   # request.FILES,
        if form.is_valid():
            identity = form.save(commit=False)
            identity.dateOfAdmission = timezone.now()
            # identity.image = form.cleaned_data['image']
            identity.save()
            return redirect('view_patientdetails', p_id=identity.pk)
    else:
        form = IdentityForm(instance=identity)
        return render(request, 'patientbasicinfo/EditIdentity.html', {'form': form})


'''  ### backup ###

@login_required
def new_identity(request):
    if request.method == "POST":
        form = IdentityForm(request.POST, request.FILES)
        if form.is_valid():
            p_identity = form.save(commit=False)
            p_identity.dateOfAdmission = timezone.now()
            p_identity.image = form.cleaned_data['image']
            p_identity.save()
            # return redirect('pbi:view_identity', p_id=p_identity.pk) # original, fix it when time comes donot delete
            return redirect('pbi:ok')
    else:
        form = IdentityForm()
    return render(request, 'patientbasicinfo/EditIdentity.html', {'form': form})

@login_required
def edit_identity(request, p_id):
    identity = get_object_or_404(Identity, pk=p_id)
    if request.method == "POST":
        form = IdentityForm(request.POST, instance=identity)
        if form.is_valid():
            identity = form.save(commit=False)
            identity.image = form.cleaned_data['image']
            identity.save()
            # return redirect('pbi:view_patientbasicinfo', p_id=identity.pk)
            return redirect('pbi:ok')
    else:
        form = IdentityForm(instance=Identity)
    context = {'form': form, 'identity': identity}
    return render(request, 'patientbasicinfo/EditIdentity.html', context)

'''
