from django import forms


class SearchByNumForm(forms.Form):  # Note that it is not inheriting from forms.ModelForm
    mobile = forms.IntegerField()
    # All my attributes here


class SearchByPkForm(forms.Form):  # Note that it is not inheriting from forms.ModelForm
    p_id = forms.IntegerField()
