from django import forms
from django.contrib.auth.models import Group


class UsuariAfegirGrup(forms.Form):
    Curs = forms.ChoiceField(
        required=True,
        choices=[[g.id, g.name] for g in Group.objects.filter()]
    )
