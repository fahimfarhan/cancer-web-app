from django import forms

from patientbasicinfo.models import Identity, Comorbidity, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class DateInput(forms.DateInput):
    input_type = 'date'


class IdentityForm(forms.ModelForm):
    religion_choice = [
        ('Not Selected', 'Not Selected'), ('Islam', 'Islam'),
        ('Hindu', 'Hindu'), ('Christian', 'Christian'),
        ('Buddhist', 'Buddhist'), ('Others', 'Others')
    ]
    gender_choice = [
        ('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')
    ]
    unit_choice = [
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')
    ]
    religion = forms.ChoiceField(widget=forms.Select, choices=religion_choice)
    gender = forms.ChoiceField(widget=forms.Select, choices=gender_choice)
    unit = forms.ChoiceField(widget=forms.Select, choices=unit_choice)

    class Meta:
        model = Identity
        fields = (
            'name', 'mobileNo', 'unit', 'gender', 'dateOfBirth', 'religion', 'address', 'referredBy', 'regNo'
        )
        widgets = {
            'dateOfBirth': DateInput()
        }


class ProfileForm(forms.ModelForm):
    bg_choice = [
        ('Not Selected', 'Not Selected'),
        ('O+', 'O+'), ('A+', 'A+'),
        ('B+', 'B+'), ('AB+', 'AB+'),
        ('O-', 'O-'), ('A-', 'A-'),
        ('B-', 'B-'), ('AB-', 'AB-'),

    ]

    bloodGroup = forms.ChoiceField(widget=forms.Select, choices=bg_choice)

    class Meta:
        model = Profile
        # fields = "__all__"
        fields = (
            'diseaseCode', 'histopathology', 'ihc', 'er_pr', 'stage', 'tnm', 'height', 'weight', 'bsa', 'ps',
            'bloodGroup'
        )


class ComorbidityForm(forms.ModelForm):
    class Meta:
        model = Comorbidity
        fields = ('hypertension', 'diabetes', 'cardiac', 'liver', 'kedney', 'others')



'''
stage_choice = [
        ('Not Selected', 'Not Selected'),
        ('stage 0', 'stage 0'),
        ('stage 1', 'stage 1'), ('stage 2', 'stage 2'),
        ('stage 3', 'stage 3'), ('stage 4', 'stage 4'),
    ]
    stage = forms.ChoiceField(widget=forms.Select, choices=stage_choice)
'''