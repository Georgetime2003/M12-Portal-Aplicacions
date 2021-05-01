from django import forms

from .models import Departament, Seminari


class DepartamentForm(forms.ModelForm):

    class Meta:
        model = Departament
        fields = ['nom']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})


class SeminariForm(forms.ModelForm):

    class Meta:
        model = Seminari
        fields = ['nom', 'places',"departament"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})
        self.fields['places'].widget.attrs.update({'class': 'form-control'})
        self.fields['departament'].widget.attrs.update({'id': 'departamentId'})
