from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Aplicacio
from .forms import ModificarGrupsAplicacioForm,ModificarEncarregatsAplicacioForm
from django.contrib.auth.models import Group , User

class AplicacioLlistatView(LoginRequiredMixin, generic.ListView):
    template_name = "aplicacions/llistar_aplicacions.html"
    context_object_name = "llista_aplicacions"
    context_object_name = "llista_aplicacions"

    def get_queryset(self):
       aplicacions =  Aplicacio.llistatAplicacions.per_usuari(self.request.user)
       return aplicacions


class AplicacioGestioLlistatView(LoginRequiredMixin, generic.ListView):
    template_name = "aplicacions/gestio_grups_encarregats/llista_aplicacions_grups_encarregats.html"
    context_object_name = "llista_aplicacions"

    def get_queryset(self):
       aplicacions =  Aplicacio.llistatAplicacions.per_usuari(self.request.user)
       return aplicacions

def AplicacioLlistatGrupsEncarregats(request,pk):
    aplicacions =  Aplicacio.llistatAplicacions.per_usuari(request.user)
    aplicacio =  Aplicacio.objects.filter(pk=pk)
    return render(request, 'aplicacions/gestio_grups_encarregats/aplicacio_grups_encarregats.html', {'llista_aplicacions': aplicacions,"aplicacio":aplicacio})



class ModificarGrupsAplicacio(generic.UpdateView):
    template_name = "aplicacions/gestio_grups_encarregats/modificar_grups_aplicacio.html"
    form_class = ModificarGrupsAplicacioForm
    queryset = Aplicacio.objects.all()

    def get_success_url(self):
        return reverse_lazy('aplicacions:llistar-grups-encarregats', kwargs={'pk': self.kwargs['pk']})


class ModificarEncarregatsAplicacio(generic.UpdateView):
    template_name = "aplicacions/gestio_grups_encarregats/modificar_encarregats_aplicacio.html"
    form_class = ModificarEncarregatsAplicacioForm
    queryset = Aplicacio.objects.all()

    def get_success_url(self):
        return reverse_lazy('aplicacions:llistar-grups-encarregats', kwargs={'pk': self.kwargs['pk']})
