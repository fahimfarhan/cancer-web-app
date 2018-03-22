from django import forms

from patientbasicinfo.models import Identity, Comorbidity, Profile, Prescription
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from tables.models import DiseaseCode


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
            'name', 'mobileNo', 'email', 'unit', 'gender', 'dateOfBirth', 'religion', 'address', 'referredBy', 'regNo'
        )
        widgets = {
            'dateOfBirth': DateInput()
        }


def get_my_choices():
    choice_list = DiseaseCode.objects.all()
    return choice_list


class ProfileForm(forms.ModelForm):
    bg_choice = [
        ('Not Selected', 'Not Selected'),
        ('O+', 'O+'), ('A+', 'A+'),
        ('B+', 'B+'), ('AB+', 'AB+'),
        ('O-', 'O-'), ('A-', 'A-'),
        ('B-', 'B-'), ('AB-', 'AB-'),

    ]

    bloodGroup = forms.ChoiceField(widget=forms.Select, choices=bg_choice)

    diseaseCode = forms.ModelChoiceField(widget=forms.Select, queryset=DiseaseCode.objects.all())

    '''def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['diseaseCode'] = forms.ChoiceField(
            choices=get_my_choices())
    '''
    class Meta:
        model = Profile
        # fields = "__all__"
        fields = (
            'diseaseCode', 'histopathology', 'ihc', 'er_pr', 'tnm', 'stage', 'height', 'weight', 'bsa', 'ps',
            'bloodGroup'
        )


class ComorbidityForm(forms.ModelForm):
    class Meta:
        model = Comorbidity
        fields = ('hypertension', 'diabetes', 'cardiac', 'liver', 'kedney', 'others')


class UploadForm(forms.ModelForm):
    class Meta:
        model = Identity
        fields = ('image',)


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('details',)
