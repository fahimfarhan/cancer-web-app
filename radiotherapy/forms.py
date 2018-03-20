from django import forms

from radiotherapy.models import RadioTherapy


class DateInput(forms.DateInput):
    input_type = 'date'


class RadioTherapyForm(forms.ModelForm):
    class Meta:
        model = RadioTherapy
        fields = (
             'intensity','dose',
             'gray', 'fractionFx', 'startDate', 'endDate')  # ekhan theke 'type' soray disi.
        widgets = {
            'startDate': DateInput(),
            'endDate' : DateInput()
        }