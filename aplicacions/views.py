from django.shortcuts import render
from .models import Aplicacio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class AplicacioLlistatView(LoginRequiredMixin, generic.ListView):
    template_name = "aplicacions/llistar_aplicacions.html"
    context_object_name = "aplicacio"
    queryset = Aplicacio.objects.all()
