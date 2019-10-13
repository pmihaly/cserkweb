from django import forms
from .models import Bejegyzes


class BejegyzesForm(forms.ModelForm):
    class Meta:
        model = Bejegyzes
        exclude = ["author", "slug"]
