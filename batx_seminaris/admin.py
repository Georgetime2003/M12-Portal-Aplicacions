from django.contrib import admin
from .models import Departament,Seminari,Solicitud,SeminariAssignat
# Register your models here.

admin.site.register(Departament)
admin.site.register(Seminari)
admin.site.register(Solicitud)
admin.site.register(SeminariAssignat)