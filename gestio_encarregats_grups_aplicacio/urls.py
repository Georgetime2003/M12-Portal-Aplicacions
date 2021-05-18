from django.urls import path
from .views import AplicacioGestioLlistatView,ModificarGrupsAplicacio,AplicacioLlistatGrupsEncarregats,ModificarEncarregatsAplicacio
app_name = "gestioEncarregatsGrups" 
urlpatterns = [
    path('', AplicacioGestioLlistatView.as_view(), name='llistat-gestio-aplicacio'),
    path('llistat_grups_encarregats/<int:pk>/', AplicacioLlistatGrupsEncarregats, name='llistar-grups-encarregats'),
    path('modificar_grups_aplicacio/<int:pk>/',ModificarGrupsAplicacio.as_view() , name='modificar-grups-aplicacio'),
    path('modificar_encarregats_aplicacio/<int:pk>/',ModificarEncarregatsAplicacio.as_view() , name='modificar-encarregats-aplicacio'),
]
