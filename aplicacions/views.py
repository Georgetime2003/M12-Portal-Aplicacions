from django.shortcuts import render
from .models import Aplicacio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from datetime import date

# Vista que mostra les aplicacions que pot gestionar el professor 
# i les aplicacions que pot accedir l'alumnat(liminat per les dates limit)
class AplicacioLlistatView(LoginRequiredMixin, generic.ListView):
    today = date.today()
    template_name = "aplicacions/llistar_aplicacions.html"
    context_object_name = "llista_aplicacions"


    def get_queryset(self):
        today = date.today()
        user = self.request.user
        if user.rol.rol == 1:
            aplicacions = Aplicacio.objects.filter(llista_encarregats__exact=user)
        else:
            aplicacions= Aplicacio.objects.filter(llista_grups__in=user.groups.all()).filter(data_limit_fi__gte=today,data_limit_inici__lte=today)
        return aplicacions


        
