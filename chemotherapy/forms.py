from django import forms

from chemotherapy.models import ChemoTherapy


class ChemoTherapyForm(forms.ModelForm):
    class Meta:
        model = ChemoTherapy
        fields = ('details',)
