from django.urls import path, include
app_name = "batxSeminaris"

from .utils import render_pdf_view
from .views import (
    MantenimentFormulari,
    AssignarProjecte,
    CrearDepartament,
    ModificarDepartament,
    EliminarDepartament,
    CrearSeminari,
    ModificarSeminari,  
    EliminarSeminari,
    EnviarSolicitud,
    get_json_seminari_data,
    get_json_departament_data,
    get_json_departament2_data,
)

urlpatterns = [
    path('',EnviarSolicitud, name='enviar-solicitud'),
    path('mantenimentFormulari/', MantenimentFormulari.as_view(), name='manteniment-formulari'),
    path('assignarProjecte/', AssignarProjecte, name='assignar-projecte'),
    path('crear_departament/', CrearDepartament.as_view(), name='crear-departament'),
    path('modificar_departament/<int:pk>/', ModificarDepartament.as_view(), name='modificar-departament'),
    path('eliminar_departament/<int:pk>/', EliminarDepartament.as_view(), name='eliminar-departament'),
    path('crear_seminari/',CrearSeminari.as_view() , name='crear-seminari'),
    path('modificar_seminari/<int:pk>/',ModificarSeminari.as_view() , name='modificar-seminari'),
    path('eliminar_seminari/<int:pk>/',EliminarSeminari.as_view() , name='eliminar-seminari'),
    
    path('seminari-json/<int:departament_id>/', get_json_seminari_data, name='seminari-json'),
    path('departament-json/<int:departament_id>/', get_json_departament_data, name='departament-json'),
    path('departament-json/<int:departament_id>/<int:departament2_id>/', get_json_departament2_data, name='departament-json2'),
    path('assignarProjecte/exportar_pdf/',render_pdf_view,name='exportar-pdf'),
]