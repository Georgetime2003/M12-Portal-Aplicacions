from django.db import models
from datetime import date

class LListaAplicacions(models.Manager): 
    def per_usuari(self, user):
        today = date.today()
        if user.is_staff:
            return self.get_queryset().all()
        if user.rol.id_rol == 1:
            return self.get_queryset().filter(llista_encarregats__exact=user)
        else:
            return self.get_queryset().filter(llista_grups__in=user.groups.all()).filter(data_limit_fi__gte=today,data_limit_inici__lte=today).distinct()
   