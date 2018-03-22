from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class SearchByNumForm(forms.Form):  # Note that it is not inheriting from forms.ModelForm
    mobile = forms.IntegerField()
    # All my attributes here


class SearchByPkForm(forms.Form):  # Note that it is not inheriting from forms.ModelForm
    p_id = forms.IntegerField()


class SearchByDate(forms.Form):  # Note that it is not inheriting from forms.ModelForm
    date = forms.DateField()
    widgets = {
        'date': DateInput()
    }

