from django.urls import path
from .views import AplicacioGestioLlistatView,ModificarGrupsAplicacio,AplicacioLlistatGrupsEncarregats
app_name = "gestioEncarregatsGrups" 
urlpatterns = [
    path('', AplicacioGestioLlistatView.as_view(), name='llistat-gestio-aplicacio'),
    path('llistat_grups_encarregats/<int:pk>/', AplicacioLlistatGrupsEncarregats, name='llistar-grups-encarregats'),
    path('modificar_encarregats_grups/<int:pk>/',ModificarGrupsAplicacio.as_view() , name='modificar-grups-encarregats'),
]
