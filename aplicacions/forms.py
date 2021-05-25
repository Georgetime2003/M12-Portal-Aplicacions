from django import forms
from django.contrib.auth.models import Group , User
from .models import Aplicacio
from django.forms import ModelMultipleChoiceField

# Formulari per modificar els grups que tenen accés a una aplicació
class ModificarGrupsAplicacioForm(forms.ModelForm):

    class Meta:
        model = Aplicacio
        fields = ['llista_grups']

    llista_grups = forms.ModelMultipleChoiceField(
        queryset = Group.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super(ModificarGrupsAplicacioForm, self).__init__(*args, **kwargs)
        self.fields['llista_grups'].required = False

# Modifica i mostra el nom complert del encarregat en el formulari
class EncarregatsMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name

# Formulari per modificar els encarregats que tenen accés a una aplicació
class ModificarEncarregatsAplicacioForm(forms.ModelForm):

    class Meta:
        model = Aplicacio
        fields = ['llista_encarregats']

    llista_encarregats = EncarregatsMultipleChoiceField(
        queryset = User.objects.filter(rol__id_rol=1),
        widget=forms.CheckboxSelectMultiple
    )
    def __init__(self, *args, **kwargs):
        super(ModificarEncarregatsAplicacioForm, self).__init__(*args, **kwargs)
        self.fields['llista_encarregats'].required = False