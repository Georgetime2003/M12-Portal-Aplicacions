from django.urls import path, include
from .views import AplicacioLlistatAlumnesView
app_name = "aplicacions"
urlpatterns = [
    path('', AplicacioLlistatAlumnesView.as_view(), name='llistat-aplicacio')
]
