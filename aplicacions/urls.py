from django.urls import path, include
from .views import (
    AplicacioLlistatView,
    ModificarGrupsAplicacio,
    AplicacioLlistatGrupsEncarregats,
    ModificarEncarregatsAplicacio 
)
app_name = "aplicacions" 
urlpatterns = [
    path('', AplicacioLlistatView.as_view(), name='llistat-aplicacio'),
    path('gestio_grups_encarregats/llistat_grups_encarregats/<int:pk>/', AplicacioLlistatGrupsEncarregats, name='llistar-grups-encarregats'),
    path('gestio_grups_encarregats/modificar_grups_aplicacio/<int:pk>/',ModificarGrupsAplicacio.as_view() , name='modificar-grups-aplicacio'),
    path('gestio_grups_encarregats/modificar_encarregats_aplicacio/<int:pk>/',ModificarEncarregatsAplicacio.as_view() , name='modificar-encarregats-aplicacio'),
]
