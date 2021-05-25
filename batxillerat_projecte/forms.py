from django import forms
from .models import Departament, Seminari

# Formulari per  afegir departaments
class DepartamentForm(forms.ModelForm):

    class Meta:
        model = Departament
        fields = ['nom']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})

# Formulari per  afegir seminaris
class SeminariForm(forms.ModelForm):

    class Meta:
        model = Seminari
        fields = ['nom', 'places','departament']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})
        self.fields['places'].widget.attrs.update({'class': 'form-control'})
        self.fields['departament'].widget.attrs.update({'id': 'departamentId','class':'d-none'})
        self.fields['departament'].label = False

# Formulari per modificar seminaris
class ModificarSeminariForm(forms.ModelForm):

    class Meta:
        model = Seminari
        fields = ['nom', 'places']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})
        self.fields['places'].widget.attrs.update({'class': 'form-control'})
