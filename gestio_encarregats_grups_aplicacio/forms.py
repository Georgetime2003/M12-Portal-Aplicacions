from django import forms
from aplicacions.models import Aplicacio
from django.contrib.auth.models import Group , User
class CreateMealForm(forms.ModelForm):

    class Meta:
        model = Aplicacio
        fields = ['llista_grups']

    llista_grups = forms.ModelMultipleChoiceField(
        queryset = Group.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )