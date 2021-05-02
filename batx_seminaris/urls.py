from django.urls import path, include
from .views import (
    MantenimentFormulari,
    AssignarProjecte,
    Assignar_Projecte,
    CrearDepartament,
    ModificarDepartament,
    EliminarDepartament,
    ModificarSeminari,  
    EliminarSeminari,
    crear_seminari,
)
app_name = "batxSeminaris"
urlpatterns = [
    path('mantenimentFormulari/', MantenimentFormulari.as_view(), name='manteniment-formulari'),
    path('assignarProjecte/', Assignar_Projecte, name='assignar-projecte'),
    path('crear_departament/', CrearDepartament.as_view(), name='crear-departament'),
    path('modificar_departament/<int:pk>/', ModificarDepartament.as_view(), name='modificar-departament'),
    path('eliminar_departament/<int:pk>/', EliminarDepartament.as_view(), name='eliminar-departament'),
    path('crear_seminari/',crear_seminari , name='crear-seminari'),
    path('modificar_seminari/<int:pk>/',ModificarSeminari.as_view() , name='modificar-seminari'),
    path('eliminar_seminari/<int:pk>/',EliminarSeminari.as_view() , name='eliminar-seminari'),
]