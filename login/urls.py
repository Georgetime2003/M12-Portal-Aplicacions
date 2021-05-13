from django.urls import path, include
from .views import GoogleLoginView, usuari_grup ,get_json_grups_data
app_name = "login"
urlpatterns = [
    path("", GoogleLoginView.as_view(), name="account_login"),
    path('grup/', usuari_grup, name='assignar-grup'),
    path('grups-json/<int:curs_id>/', get_json_grups_data, name='curs-json'),
]
