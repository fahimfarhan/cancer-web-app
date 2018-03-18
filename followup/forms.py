from django import forms

from followup.models import FollowUp

class DateInput(forms.DateInput):
    input_type = 'date'


class FollowUpForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        fields = ('date', 'details',)
        widgets = {
            'date': DateInput()
        }
