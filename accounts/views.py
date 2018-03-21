from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from accounts.forms import RegistrationForm, EditProfileForm
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
