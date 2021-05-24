from django.core.exceptions import PermissionDenied
from aplicacions.models import Aplicacio

def professor_encarregat(view_func):
    def func(request, *args, **kwargs):
        aplicacio = Aplicacio.objects.filter(pk=kwargs['pk'])
        llistaEncarregats = aplicacio[0].llista_encarregats.all()
        if request.user in llistaEncarregats or request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return func