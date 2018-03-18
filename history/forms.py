from django import forms

from history.models import HistoryModel, HistoryModelFile


class HistoryForm(forms.ModelForm):
    class Meta:
        model = HistoryModel
        fields = (
            'details', 'notes',
        )


class UploadForm(forms.ModelForm):
    class Meta:
        model = HistoryModelFile
        fields = ('file',)
