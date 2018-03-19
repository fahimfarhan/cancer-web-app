from django import forms

from surgeryhormone.models import Surgery, Hormone


class SurgeryForm(forms.ModelForm):
    class Meta:
        model = Surgery
        fields = ('details',)


class HormoneForm(forms.ModelForm):
    class Meta:
        model = Hormone
        fields = ('details',)
