from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from aplicacions.models import Aplicacio
from django.contrib.auth.models import Group , User
from .forms import CreateMealForm
from django.urls import reverse_lazy

# Create your views here.
class AplicacioGestioLlistatView(LoginRequiredMixin, generic.ListView):
    template_name = "gestio_encarregats_grups_aplicacio/llista_aplicacions_grups_encarregats.html"
    context_object_name = "llista_aplicacions"

    def get_queryset(self):
       aplicacions =  Aplicacio.llistatAplicacions.per_usuari(self.request.user)
       return aplicacions

def AplicacioLlistatGrupsEncarregats(request,pk):
    aplicacions =  Aplicacio.llistatAplicacions.per_usuari(request.user)
    aplicacio =  Aplicacio.objects.filter(pk=pk)
    return render(request, 'gestio_encarregats_grups_aplicacio/aplicacio_grups_encarregats.html', {'llista_aplicacions': aplicacions,"aplicacio":aplicacio})



class ModificarGrupsAplicacio(generic.UpdateView):
    template_name = "gestio_encarregats_grups_aplicacio/modificar_grups_encarregats.html"
    form_class = CreateMealForm
    queryset = Aplicacio.objects.all()

    def get_success_url(self):
        return reverse_lazy('gestioEncarregatsGrups:llistar-grups-encarregats', kwargs={'pk': self.kwargs['pk']})

