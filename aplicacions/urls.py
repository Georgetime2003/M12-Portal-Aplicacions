from django.urls import path, include
from .views import AplicacioLlistatView
app_name = "aplicacions"
urlpatterns = [
    path('', AplicacioLlistatView.as_view(), name='llistat-aplicacio')
]
