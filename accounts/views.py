from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from accounts.forms import RegistrationForm, EditProfileForm, EditDoctorForm
from accounts.models import Doctor
from analytics.forms import SearchByNumForm, SearchByPkForm


@login_required
def home(request):
    form = SearchByNumForm()
    form_pk = SearchByPkForm()
    context = {'form':form, 'form_pk':form_pk}
    return render(request, 'accounts/home.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)  # UserCreationForm
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()  #
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


@login_required
def edit_doctorinfo(request):
    if not Doctor.objects.filter(identity_fk=request.user).exists():
        return new_doctorinfo(request)
    else:
        doctor = get_object_or_404(Doctor, identity_fk=request.user)
        if request.method == 'POST':
            form = EditDoctorForm(request.POST, instance=doctor)
            if form.is_valid():
                form.save()
                return redirect('view_doctorinfo')
        else:
            form = EditDoctorForm(instance=doctor)
            args = {'form': form}
            return render(request, 'accounts/edit_doctorinfo.html', args)


@login_required
def new_doctorinfo(request):
    if request.method == 'POST':
        form = EditDoctorForm(request.POST)  # UserCreationForm
        if form.is_valid():
            p_doctor = form.save(commit=False)
            p_doctor.identity_fk = request.user
            p_doctor.save()
            return redirect('view_doctorinfo')
    else:
        form = EditDoctorForm()  #
        args = {'form': form}
        return render(request, 'accounts/edit_doctorinfo.html', args)


@login_required
def view_doctorinfo(request):
    if not Doctor.objects.filter(identity_fk=request.user).exists():
        doctor = None
    else:
        doctor = get_object_or_404(Doctor, identity_fk=request.user)
    args = {'doctor': doctor}
    return render(request, 'accounts/view_doctorinfo.html', args)
