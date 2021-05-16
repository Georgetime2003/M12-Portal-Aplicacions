from django.contrib import admin
from .models import Departament, Seminari, Solicitud

admin.site.register(Departament)


@admin.register(Seminari)
class SeminariAdmin(admin.ModelAdmin):
    list_display = ['nom', 'places']

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ['usuari', 'seminari','assignat']
