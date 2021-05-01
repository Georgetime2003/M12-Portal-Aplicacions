from django.urls import path, include
from .views import (
    MantenimentFormulari,
    AfegirDepartament,
    ModificarDepartament,
    EliminarDepartament,
    AfegirSeminari,
    ModificarSeminari,  
    EliminarSeminari,  
)
app_name = "batxSeminaris"
urlpatterns = [
    path('', MantenimentFormulari.as_view(), name='manteniment-formulari'),
    path('afegir_departament/', AfegirDepartament.as_view(), name='afegir-departament'),
    path('modificar_departament/<int:pk>/', ModificarDepartament.as_view(), name='modificar-departament'),
    path('eliminar_departament/<int:pk>/', EliminarDepartament.as_view(), name='eliminar-departament'),
    path('afegir_seminari/<int:pk>/',AfegirSeminari.as_view() , name='afegir-seminari'),
    path('modificar_seminari/<int:pk>/',ModificarSeminari.as_view() , name='modificar-seminari'),
    path('eliminar_seminari/<int:pk>/',EliminarSeminari.as_view() , name='eliminar-seminari'),
]