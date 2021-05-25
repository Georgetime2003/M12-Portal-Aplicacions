from django.core.exceptions import PermissionDenied
from aplicacions.models import Aplicacio
# Decorator que comproba si l'usuari es troba en la llista d'encarregats de 
# l'aplicacio batxillerat_projecte

def professor_encarregat(view_func):
    aplicacio = Aplicacio.objects.filter(pk=1)
    llistaEncarregats = aplicacio[0].llista_encarregats.all()

    def func(request, *args, **kwargs):
        if request.user in llistaEncarregats or request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return func

def usuari_grup_aplicacio(view_func):
    aplicacio = Aplicacio.objects.filter(pk=1)
    llistaGrups = aplicacio[0].llista_grups.all()
    def func(request, *args, **kwargs):
        if request.user.groups.first() in llistaGrups or request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return func