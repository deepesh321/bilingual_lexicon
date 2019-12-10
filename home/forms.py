from django import forms
from .models import Corpora

class CorporaForm(forms.ModelForm):
    class Meta:
        model = Corpora
        fields = ('lang1','lang2')