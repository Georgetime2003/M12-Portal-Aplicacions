from django import forms

from .models import Departament

class DepartamentForm(forms.ModelForm):

    class Meta:
        model = Departament
        fields = ['nom']
    