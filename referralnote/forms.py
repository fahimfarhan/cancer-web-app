from django import forms

from referralnote.models import ReferralNote


class ReferralNoteForm(forms.ModelForm):
    class Meta:
        model = ReferralNote
        fields = (
            'purpose','condition', 'refferedDept', 'refferedConsultant', 'responseNote', 'remarks'
        )
