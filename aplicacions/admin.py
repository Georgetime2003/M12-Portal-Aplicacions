from django.contrib import admin
from .models import Aplicacio

@admin.register(Aplicacio)
class Aplicacio(admin.ModelAdmin):
    list_display = ['nom', 'descripcio']