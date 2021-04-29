from django.urls import path, include
from .views import  MantenimentFormulari,AfegirDepartament
app_name = "batxSeminaris"
urlpatterns = [
    path('', MantenimentFormulari.as_view(), name='manteniment-formulari'),
    path('afegir_departament/', AfegirDepartament.as_view(), name='afegir-departament')
]