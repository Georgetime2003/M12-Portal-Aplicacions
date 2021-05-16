from django.contrib import admin
from .models import Curs,Group,Rol
from django.contrib import admin

admin.site.register(Curs)
admin.site.register(Group)
@admin.register(Rol)
class Rol(admin.ModelAdmin):
    list_display = ['user', 'id_rol']

