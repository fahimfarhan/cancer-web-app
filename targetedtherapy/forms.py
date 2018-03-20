
from django import forms

from targetedtherapy.models import Tki, Immunotherapy


class TkiForm(forms.ModelForm):
    class Meta:
        model = Tki
        fields =('details',)


class ImmunotherapyForm(forms.ModelForm):
    class Meta:
        model = Immunotherapy
        fields = ('details',)


