from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Aplicacio

class AplicacioLlistatView(LoginRequiredMixin, generic.ListView):
    template_name = "aplicacions/llistar_aplicacions.html"
    context_object_name = "llista_aplicacions"

    def get_queryset(self):
       aplicacions =  Aplicacio.llistatAplicacions.per_usuari(self.request.user)
       return aplicacions