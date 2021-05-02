from django.shortcuts import render , get_object_or_404 ,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import Departament, Seminari, Solicitud
from .forms import DepartamentForm, SeminariForm
from django.db.models.query import QuerySet
from collections import defaultdict



class MantenimentFormulari(LoginRequiredMixin, generic.ListView):
    template_name = "batx_seminaris/manteniment_formulari.html"
    context_object_name = "llista_manteniment"
    queryset = Departament.objects.all()


def Assignar_Projecte(request):
    Solicituds = Solicitud.objects.all()
    a={}
    for solicitud in Solicituds:
        a.setdefault(solicitud.usuari_id, []).append(solicitud)
    
    print(a)
    return render(request,'batx_seminaris/assignar_projecte.html',{"solicituds": sorted(a.items())})
    

class AssignarProjecte(LoginRequiredMixin, generic.ListView):
    template_name = "batx_seminaris/assignar_projecte.html"
    context_object_name = "llista_solicituds"
    ArraySolicituds=[]
    query = Solicitud.objects.all()
    a={}
    for solicitud in query:
        a.setdefault(solicitud.usuari_id, []).append(solicitud)
    ArraySolicituds.append(a)
    queryset = ArraySolicituds
            
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

class ModificarSeminari(LoginRequiredMixin, generic.UpdateView):
    template_name = "batx_seminaris/seminari_crud/modificar_seminari.html"
    form_class = SeminariForm
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")
    queryset = Seminari.objects.all()

class EliminarSeminari(LoginRequiredMixin, generic.DeleteView):
    template_name = "batx_seminaris/seminari_crud/eliminar_seminari.html"
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")
    queryset = Seminari.objects.all()


def crear_seminari(request):
    if request.method == "POST":
        form = SeminariForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/batxilleratProjecte/mantenimentFormulari/")
    else:
        form= SeminariForm()
        return render(request, 'batx_seminaris/seminari_crud/crear_seminari.html',{"form":form})
