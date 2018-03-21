from django import forms

from tables.models import NactCycle, ActCycle, ConcurrentCycle, PalliativeCycle, CobaltChart, LinacChart, BrachyChart


class NactCycleForm(forms.ModelForm):
    class Meta:
        model = NactCycle
        exclude = ('cycle', 'nact_fk',)


class ActCycleForm(forms.ModelForm):
    class Meta:
        model = ActCycle
        exclude = ('cycle', 'act_fk',)


class ConcurrentCycleForm(forms.ModelForm):
    class Meta:
        model = ConcurrentCycle
        exclude = ('cycle', 'concurr_fk',)


class PalliativeCycleForm(forms.ModelForm):
    class Meta:
        model = PalliativeCycle
        exclude = ('cycle', 'palliative_fk',)


class CobaltChartForm(forms.ModelForm):
    class Meta:
        model = CobaltChart
        exclude = ('serialno', 'cobalt_fk',)


class LinacChartForm(forms.ModelForm):
    class Meta:
        model = LinacChart
        exclude = ('serialno', 'linac_fk',)


class BrachyChartForm(forms.ModelForm):
    class Meta:
        model = BrachyChart
        exclude = ('serialno', 'brachy_fk',)
