from django.shortcuts import render , get_object_or_404 ,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from aplicacions.models import Aplicacio
from .models import Departament, Seminari, Solicitud
from .forms import DepartamentForm, SeminariForm,ModificarSeminariForm
from django.db.models.query import QuerySet
from collections import defaultdict
from django.http import JsonResponse



class MantenimentFormulari(LoginRequiredMixin, generic.ListView):
    template_name = "batx_seminaris/manteniment_formulari.html"
    context_object_name = "llista_manteniment"
    queryset = Departament.objects.all()

class AssignarProjecte(LoginRequiredMixin, generic.ListView):
    template_name = "batx_seminaris/assignar_projecte.html"
    context_object_name = "llista_solicituds"
    Solicituds = Solicitud.objects.all()
    a={}
    for solicitud in Solicituds:
        a.setdefault(solicitud.usuari_id, []).append(solicitud)

    queryset = sorted(a.items())


class CrearDepartament(LoginRequiredMixin, generic.CreateView):
    template_name = "batx_seminaris/departament_crud/crear_departament.html"
    form_class = DepartamentForm
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")


class ModificarDepartament(LoginRequiredMixin, generic.UpdateView):
    template_name = "batx_seminaris/departament_crud/modificar_departament.html"
    form_class = DepartamentForm
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")
    queryset = Departament.objects.all()


class EliminarDepartament(LoginRequiredMixin, generic.DeleteView):
    template_name = "batx_seminaris/departament_crud/eliminar_departament.html"
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")
    queryset = Departament.objects.all()


class CrearSeminari(LoginRequiredMixin, generic.CreateView):
    template_name = "batx_seminaris/seminari_crud/crear_seminari.html"
    form_class = SeminariForm
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")

class ModificarSeminari(LoginRequiredMixin, generic.UpdateView):
    template_name = "batx_seminaris/seminari_crud/modificar_seminari.html"
    form_class = ModificarSeminariForm
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")
    queryset = Seminari.objects.all()

class EliminarSeminari(LoginRequiredMixin, generic.DeleteView):
    template_name = "batx_seminaris/seminari_crud/eliminar_seminari.html"
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")
    queryset = Seminari.objects.all()

#View pagina principal solicitud
def EnviarSolicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
           
            return HttpResponseRedirect('/thanks/')
    else:
        aplicacions = Aplicacio.objects.all()
        departaments = Departament.objects.values()
        departaments2 = Departament.objects.exclude(id=1).values()
        print(departaments2)
    return render(request, 'batx_seminaris/enviar_solicitud.html', {'llista_aplicacions':aplicacions,'llista_departaments':departaments})

def get_json_seminari_data(request, *args, **kwargs):
    selected_departament = kwargs.get('departament_id')
    obj_seminaris = list(Seminari.objects.filter(departament__id=selected_departament).values())
    return JsonResponse({'data':obj_seminaris})

def get_json_departament_data(request, *args, **kwargs):
    selected_departament = kwargs.get('departament_id')
    obj_departaments = list(Departament.objects.exclude(id=selected_departament).values())
    return JsonResponse({'data':obj_departaments})
