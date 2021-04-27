from django.urls import path, include
from .views import  MantenimentFormulari
app_name = "batxSeminaris"
urlpatterns = [
    path('', MantenimentFormulari.as_view(), name='manteniment-formulari')
]