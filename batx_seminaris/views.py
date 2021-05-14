from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models import Count,Case,When,F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required,permission_required
from aplicacions.models import Aplicacio
from .models import Departament, Seminari, Solicitud
from .forms import DepartamentForm, SeminariForm,ModificarSeminariForm
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Vista d'acces al manteniment del formulari
class MantenimentFormulari(PermissionRequiredMixin,LoginRequiredMixin, generic.ListView):
    permission_required = 'batx_seminaris.gestio_professor'
    template_name = "batx_seminaris/manteniment_formulari.html"
    context_object_name = "llista_manteniment"
    queryset = Departament.objects.all()

# Vista d'acces per assignar projecte als alumnes
@login_required
@permission_required('batx_seminaris.gestio_professor',raise_exception=True)
def AssignarProjecte(request):
    if request.method == 'POST':
        solicitudId = request.POST.get('solicitudId')
        usuariId = request.POST.get('usuariId')
        
        SolicitudsUsuari = Solicitud.objects.filter(usuari_id=usuariId)
        SolicitudsUsuari.filter(assignat=True).update(assignat=False)
        SolicitudsUsuari.filter(id=solicitudId).update(assignat=True)
        placesDisponibles = list(Solicitud.objects.values('seminari').annotate(num_places=F('seminari__places')-Count(Case(When(assignat=True, then=1)))))
        return JsonResponse({'data':placesDisponibles})
    else:
        Solicituds = Solicitud.objects.all()
        placesDisponibles = Solicitud.objects.values('seminari').annotate(num_places=F('seminari__places')-Count(Case(When(assignat=True, then=1))))
        solicitudsPerId={}
        for solicitud in Solicituds:
            solicitudsPerId.setdefault(solicitud.usuari_id, []).append(solicitud)
        llistaSolicitudsId = sorted(solicitudsPerId.items())
        
        return render(request, 'batx_seminaris/assignar_projecte.html', {'llista_solicituds': llistaSolicitudsId,'placesDisponibles':placesDisponibles})

# Vista modal per crear departament
class CrearDepartament(PermissionRequiredMixin,LoginRequiredMixin, generic.CreateView):
    permission_required = 'batx_seminaris.gestio_professor'
    template_name = "batx_seminaris/departament_crud/crear_departament.html"
    form_class = DepartamentForm
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")

# Vista modal per modificar departament
class ModificarDepartament(PermissionRequiredMixin,LoginRequiredMixin, generic.UpdateView):
    permission_required = 'batx_seminaris.gestio_professor'
    template_name = "batx_seminaris/departament_crud/modificar_departament.html"
    form_class = DepartamentForm
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")
    queryset = Departament.objects.all()

# Vista modal per eliminar departament
class EliminarDepartament(PermissionRequiredMixin,LoginRequiredMixin, generic.DeleteView):
    permission_required = 'batx_seminaris.gestio_professor'
    template_name = "batx_seminaris/departament_crud/eliminar_departament.html"
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")
    queryset = Departament.objects.all()

# Vista modal per crear seminari
class CrearSeminari(PermissionRequiredMixin,LoginRequiredMixin, generic.CreateView):
    permission_required = 'batx_seminaris.gestio_professor'
    template_name = "batx_seminaris/seminari_crud/crear_seminari.html"
    form_class = SeminariForm
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")

# Vista modal per modificar seminari
class ModificarSeminari(PermissionRequiredMixin,LoginRequiredMixin, generic.UpdateView):
    permission_required = 'batx_seminaris.gestio_professor'
    template_name = "batx_seminaris/seminari_crud/modificar_seminari.html"
    form_class = ModificarSeminariForm
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")
    queryset = Seminari.objects.all()

# Vista modal per eliminar seminari
class EliminarSeminari(PermissionRequiredMixin,LoginRequiredMixin, generic.DeleteView):
    permission_required = 'batx_seminaris.gestio_professor'
    template_name = "batx_seminaris/seminari_crud/eliminar_seminari.html"
    success_url = reverse_lazy("batxSeminaris:manteniment-formulari")
    queryset = Seminari.objects.all()

# Vista per generar un pdf amb el llistat d'alumnes i seminari assignat
@permission_required('batx_seminaris.gestio_professor',raise_exception=True)
def render_pdf_view(request):
    template_path = 'batx_seminaris/exportar_pdf.html'
    llistaSolicituds =  Solicitud.objects.filter(assignat=True)
    context = {'llistaSolicituds': llistaSolicituds}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="llistaAssignacioProjecte.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



# View pagina principal solicitud
@login_required
@permission_required("batx_seminaris.enviar_solicitud",raise_exception=True)
def EnviarSolicitud(request):
    if request.method == 'POST':
        user = request.user
        seminariPrimeraOpcio = request.POST.get('seminariPrimeraOpcio')
        seminariSegonaOpcio = request.POST.get('seminariSegonaOpcio')
        seminariTerceraOpcio = request.POST.get('seminariTerceraOpcio')

        seminariOpcio1 = Seminari.objects.get(pk=seminariPrimeraOpcio)
        seminariOpcio2 = Seminari.objects.get(pk=seminariSegonaOpcio)
        seminariOpcio3 = Seminari.objects.get(pk=seminariTerceraOpcio)

        solicitud = Solicitud()
        solicitud2 = Solicitud()
        solicitud3 = Solicitud()

        solicitud.seminari = seminariOpcio1
        solicitud.usuari = user
        solicitud.plantajament = request.POST.get('plantajamentPrimeraOpcio')
        solicitud.save()

        solicitud2.seminari = seminariOpcio2
        solicitud2.usuari = user
        solicitud2.plantajament = request.POST.get('plantajamentSegonaOpcio')
        solicitud2.save()

        solicitud3.seminari = seminariOpcio3
        solicitud3.usuari = user
        solicitud3.plantajament = request.POST.get('plantajamentTerceraOpcio')
        solicitud3.save()
        return JsonResponse({'success': True}, status=201)
    else:
        aplicacions = Aplicacio.objects.all()
        countSolicituds =  Solicitud.objects.filter(usuari=request.user).count()
        if(countSolicituds >=3):
            return render(request, 'batx_seminaris/solicitud_enviada.html',{'llista_aplicacions':aplicacions})
        else:    
            aplicacions = Aplicacio.objects.all()
            departaments = Departament.objects.values()
            return render(request, 'batx_seminaris/enviar_solicitud.html', {'llista_aplicacions':aplicacions,'llista_departaments':departaments})

# vista que retorna un dicionari de seminaris a partir d'un departament
def get_json_seminari_data(request, *args, **kwargs):
    selected_departament = kwargs.get('departament_id')
    obj_seminaris = list(Seminari.objects.filter(departament__id=selected_departament).values())
    return JsonResponse({'data':obj_seminaris})

# vista que retorna un dicionari de departaments  diferent al departament selecionat anteriorment
def get_json_departament_data(request, *args, **kwargs):
    selected_departament = kwargs.get('departament_id')
    obj_departaments = list(Departament.objects.exclude(id=selected_departament).values())
    return JsonResponse({'data':obj_departaments})

# vista que retorna un dicionari de departaments  diferent als dos departament selecionats anteriorment
def get_json_departament2_data(request, *args, **kwargs):
    selected_departament = kwargs.get('departament_id')
    selected_departament2 = kwargs.get('departament2_id')
    ex=[selected_departament,selected_departament2]
    obj_departaments = list(Departament.objects.exclude(id__in=ex).values())
    return JsonResponse({'data':obj_departaments})