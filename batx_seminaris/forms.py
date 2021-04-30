from django import forms

from .models import Departament

class DepartamentForm(forms.ModelForm):

    class Meta:
        model = Departament
        fields = ['nom']
        widget=forms.Select(attrs={"class": "form-select"})
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control'})
        