from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from .models import Aplicacio
from .forms import ModificarGrupsAplicacioForm,ModificarEncarregatsAplicacioForm
from django.utils.decorators import method_decorator
from .decorators import professor_encarregat

# View que mostra les aplicacions als usuaris
class AplicacioLlistatView(LoginRequiredMixin, generic.ListView):
    template_name = "aplicacions/llistar_aplicacions.html"
    context_object_name = "llista_aplicacions"

    def get_queryset(self):
       aplicacions =  Aplicacio.llistatAplicacions.per_usuari(self.request.user)
       return aplicacions

# View que mostra ens encarregats i els grups d'una aplicació
@login_required
@professor_encarregat
def AplicacioLlistatGrupsEncarregats(request,pk):

    aplicacions =  Aplicacio.llistatAplicacions.per_usuari(request.user)
    aplicacio =  Aplicacio.objects.filter(pk=pk)
    return render(request, 'aplicacions/gestio_grups_encarregats/aplicacio_grups_encarregats.html', {'llista_aplicacions': aplicacions,"aplicacio":aplicacio})


# View per modificar els grups d'una aplicació
class ModificarGrupsAplicacio(LoginRequiredMixin,generic.UpdateView):

    @method_decorator(professor_encarregat)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    template_name = "aplicacions/gestio_grups_encarregats/modificar_grups_aplicacio.html"
    form_class = ModificarGrupsAplicacioForm
    queryset = Aplicacio.objects.all()

    def get_success_url(self):
        return reverse_lazy('aplicacions:llistar-grups-encarregats', kwargs={'pk': self.kwargs['pk']})

# View per modificar els encarregats d'una aplicació
class ModificarEncarregatsAplicacio(LoginRequiredMixin,generic.UpdateView):
    
    @method_decorator(professor_encarregat)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    template_name = "aplicacions/gestio_grups_encarregats/modificar_encarregats_aplicacio.html"
    form_class = ModificarEncarregatsAplicacioForm
    queryset = Aplicacio.objects.all()

    def get_success_url(self):
        return reverse_lazy('aplicacions:llistar-grups-encarregats', kwargs={'pk': self.kwargs['pk']})
