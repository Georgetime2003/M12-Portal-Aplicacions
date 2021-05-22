from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from aplicacions.models import Aplicacio
def professor_encarregat(view_func):
    aplicacio = Aplicacio.objects.filter(pk=1)
    llistaEncarregats = aplicacio[0].llista_encarregats.all()

    def func(request, *args, **kwargs):
        if request.user in llistaEncarregats or request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return func