from django import forms
from django.contrib.auth.models import Group , User
from .models import Aplicacio

class ModificarGrupsAplicacioForm(forms.ModelForm):

    class Meta:
        model = Aplicacio
        fields = ['llista_grups']

    llista_grups = forms.ModelMultipleChoiceField(
        queryset = Group.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class ModificarEncarregatsAplicacioForm(forms.ModelForm):

    class Meta:
        model = Aplicacio
        fields = ['llista_encarregats']

    llista_encarregats = forms.ModelMultipleChoiceField(
        queryset = User.objects.filter(rol__id_rol=1),
        widget=forms.CheckboxSelectMultiple
    )