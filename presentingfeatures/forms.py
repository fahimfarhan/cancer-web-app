from django import forms

from presentingfeatures.models import Status, Investigation


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('details', 'advice')


class UploadForm(forms.ModelForm):
    type_choice = [
        ('Others', 'Others'), ('Marker', 'Marker'),
        ('X-ray', 'X-ray'), ('USG', 'USG'),
        ('CT-Scan', 'CT-Scan'), ('MRI', 'MRI'),
        ('MRS', 'MRS'), ('PET', 'PET'),
        ('Echo', 'Echo'),
        ('CBC', 'CBC'), ('RBS', 'RBS'), ('LFT', 'LFT'), ('KFT', 'KFT'),
        ('Serum-Electrolytes', 'Serum-Electrolytes'),

    ]

    type = forms.ChoiceField(widget=forms.Select, choices=type_choice)

    class Meta:
        model = Investigation
        fields = ('type', 'file',)
