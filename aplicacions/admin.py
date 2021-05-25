from django.contrib import admin
from .models import Aplicacio
from django.contrib.auth.models import Group

@admin.register(Aplicacio)
class Aplicacio(admin.ModelAdmin):
    list_display = ['nom', 'descripcio','id']
    filter_horizontal  = ("llista_grups","llista_encarregats")

admin.site.unregister(Group)