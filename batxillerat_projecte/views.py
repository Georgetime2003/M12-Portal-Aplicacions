from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models import Count,Case,When,F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required,permission_required
from aplicacions.models import Aplicacio
from autenticacio.models import Group
from .models import Departament, Seminari, Solicitud
from .forms import DepartamentForm, SeminariForm,ModificarSeminariForm
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from .decorators import professor_encarregat,usuari_grup_aplicacio
# Vista d'acces al manteniment del formulari
class MantenimentFormulari(LoginRequiredMixin, generic.ListView):

    @method_decorator(professor_encarregat)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    template_name = "batx_seminaris/manteniment_formulari.html"
    context_object_name = "llista_manteniment"
    queryset = Departament.objects.all()

# Vista d'acces per assignar projecte als alumnes
@login_required
@professor_encarregat
def AssignarProjecte(request):
    if request.method == 'POST':
        # Al usuari si assigna el seminari i es retorna una llista amb les places recalculades
        solicitudId = request.POST.get('solicitudId')
        usuariId = request.POST.get('usuariId')
        SolicitudsUsuari = Solicitud.objects.filter(usuari_id=usuariId)
        SolicitudsUsuari.filter(assignat=True).update(assignat=False)
        SolicitudsUsuari.filter(id=solicitudId).update(assignat=True)
        placesDisponibles = list(Solicitud.objects.values('seminari').annotate(num_places=F('seminari__places')-Count(Case(When(assignat=True, then=1)))))
        return JsonResponse({'data':placesDisponibles})
    else:
        Solicituds = Solicitud.objects.all()
        grups= Group.objects.filter(curs=3)
        placesDisponibles = Solicitud.objects.values('seminari').annotate(num_places=F('seminari__places')-Count(Case(When(assignat=True, then=1))))
        solicitudsPerId={}
        # Crea objecte amb usuari id de clau i de data les seves solicituds.
        for solicitud in Solicituds:
            solicitudsPerId.setdefault(solicitud.usuari_id, []).append(solicitud)
        llistaSolicitudsId = sorted(solicitudsPerId.items())
        
        return render(request, 'batx_seminaris/assignar_projecte.html', {'llista_solicituds': llistaSolicitudsId,'placesDisponibles':placesDisponibles,"llista_grups":grups})

# Vista modal per crear departament
class CrearDepartament(LoginRequiredMixin, generic.CreateView):

    @method_decorator(professor_encarregat)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    template_name = "batx_seminaris/departament_crud/crear_departament.html"
    form_class = DepartamentForm
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")

# Vista modal per modificar departament
class ModificarDepartament(LoginRequiredMixin, generic.UpdateView):
    
    @method_decorator(professor_encarregat)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    template_name = "batx_seminaris/departament_crud/modificar_departament.html"
    form_class = DepartamentForm
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")
    queryset = Departament.objects.all()

# Vista modal per eliminar departament
class EliminarDepartament(LoginRequiredMixin, generic.DeleteView):
    
    @method_decorator(professor_encarregat)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    template_name = "batx_seminaris/departament_crud/eliminar_departament.html"
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")
    queryset = Departament.objects.all()

# Vista modal per crear seminari
class CrearSeminari(LoginRequiredMixin, generic.CreateView):
    
    @method_decorator(professor_encarregat)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    template_name = "batx_seminaris/seminari_crud/crear_seminari.html"
    form_class = SeminariForm
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")

# Vista modal per modificar seminari
class ModificarSeminari(LoginRequiredMixin, generic.UpdateView):
    
    @method_decorator(professor_encarregat)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    template_name = "batx_seminaris/seminari_crud/modificar_seminari.html"
    form_class = ModificarSeminariForm
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")
    queryset = Seminari.objects.all()

# Vista modal per eliminar seminari
class EliminarSeminari(LoginRequiredMixin, generic.DeleteView):

    @method_decorator(professor_encarregat)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    template_name = "batx_seminaris/seminari_crud/eliminar_seminari.html"
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")
    queryset = Seminari.objects.all()


# View pagina principal solicitud
@login_required
@usuari_grup_aplicacio
def EnviarSolicitud(request):
    if request.method == 'POST':
        user = request.user
        seminariPrimeraOpcio = request.POST.get('seminariPrimeraOpcio')
        seminariSegonaOpcio = request.POST.get('seminariSegonaOpcio')
        seminariTerceraOpcio = request.POST.get('seminariTerceraOpcio')

        seminariOpcio1 = get_object_or_404(Seminari, pk=seminariPrimeraOpcio)
        seminariOpcio2 = get_object_or_404(Seminari, pk=seminariSegonaOpcio)
        seminariOpcio3 = get_object_or_404(Seminari, pk=seminariTerceraOpcio)

        solicitud = Solicitud(seminari=seminariOpcio1,usuari=user,plantajament=request.POST.get('plantajamentPrimeraOpcio'))
        solicitud.save()

        solicitud2 = Solicitud(seminari=seminariOpcio2,usuari=user,plantajament=request.POST.get('plantajamentSegonaOpcio'))
        solicitud2.save()


        solicitud3 = Solicitud(seminari=seminariOpcio3,usuari=user,plantajament=request.POST.get('plantajamentSegonaOpcio'))
        solicitud3.save()

        return JsonResponse({'success': True}, status=201)
    else:
        aplicacions = Aplicacio.llistatAplicacions.per_usuari(request.user)
        solicituds =  Solicitud.objects.filter(usuari=request.user)
        if(solicituds.count() >=3):
            return render(request, 'batx_seminaris/solicitud_enviada.html',{'llista_aplicacions':aplicacions,"llista_solicituds":solicituds})
        else:    
            departaments = Departament.objects.values()
            return render(request, 'batx_seminaris/enviar_solicitud.html', {'llista_aplicacions':aplicacions,'llista_departaments':departaments})

# vista que retorna un dicionari de seminaris a partir d'un departament
@login_required
def get_json_seminari_data(request, *args, **kwargs):
    selected_departament = kwargs.get('departament_id')
    obj_seminaris = list(Seminari.objects.filter(departament__id=selected_departament).values())
    return JsonResponse({'data':obj_seminaris})
@login_required
# vista que retorna un dicionari de departaments  diferent al departament selecionat anteriorment
def get_json_departament_data(request, *args, **kwargs):
    selected_departament = kwargs.get('departament_id')
    obj_departaments = list(Departament.objects.exclude(id=selected_departament).values())
    return JsonResponse({'data':obj_departaments})
@login_required
# vista que retorna un dicionari de departaments  diferent als dos departament selecionats anteriorment
def get_json_departament2_data(request, *args, **kwargs):
    selected_departament = kwargs.get('departament_id')
    selected_departament2 = kwargs.get('departament2_id')
    ex=[selected_departament,selected_departament2]
    obj_departaments = list(Departament.objects.exclude(id__in=ex).values())
    return JsonResponse({'data':obj_departaments})