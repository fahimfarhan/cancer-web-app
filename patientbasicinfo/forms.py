from django import forms

from patientbasicinfo.models import Identity, Comorbidity
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


class ComorbidityForm(forms.ModelForm):
    class Meta:
        model = Comorbidity
        fields = ('hypertension', 'diabetes', 'cardiac', 'liver', 'kedney', 'others')
