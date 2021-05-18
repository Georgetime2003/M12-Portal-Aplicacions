from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('autenticacio.urls', namespace="autenticacio")),
    path('aplicacions/', include('aplicacions.urls', namespace="aplicacions")),
    path('aplicacions/projecte_batxillerat/', include('batxillerat_projecte.urls', namespace="batxSeminaris")),
    path('aplicacions/gestio_grups_encarregats/', include('gestio_encarregats_grups_aplicacio.urls', namespace="gestioEncarregatsGrups")),
    # Path obligatori allauth
    path('accounts/', include('allauth.urls')),
]
