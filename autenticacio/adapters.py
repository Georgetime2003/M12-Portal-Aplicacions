from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import render
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import Rol
   
# Comprova que el domini del correu sigui @sapalomera.
class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    
    def pre_social_login(self, request, sociallogin):
        email = sociallogin.user.email.lower().split("@")
        error = "La compte de correu ha de ser domini sapalomera '@sapalomera.cat' "
        if email[1] != "sapalomera.cat":
            raise ImmediateHttpResponse(
                render(request,"login/login.html", {'error': error})
            )


class AdapterCustom(DefaultAccountAdapter):

    # Funcio que redirigeix al registrase, si es un usuari a la view per escollir grup
    # Si l'usuari es professor a aplicacions
    def get_signup_redirect_url(self, request):
        if request.user.rol.id_rol == 2:
            path = "/grup/"
        else:
            path = "/aplicacions/"
        return path

    # Funcio que redirigeix al login, si es un usuari a la view per escollir grup
    # Si l'usuari es professor a aplicacions
    def get_login_redirect_url(self, request):
        grups = request.user.groups.all()
        if request.user.is_staff or request.user.rol.id_rol == 1 :
            path = "/aplicacions/"
            return path
            
        if not grups:
            path = "/grup/"
            return path
        else:
            path = "/aplicacions/"
            return path

#Afegeix el rol a l'usuari un cop creada la compte
@receiver(user_signed_up)
def retrieve_social_data(request, user, **kwargs):
    email= user.email.lower().split("@")
    if email[0].find(".") != -1:
        usuariRol = Rol(user=user,id_rol=2)
        usuariRol.save()
    else:
        usuariRol = Rol(user=user,id_rol=1)
        usuariRol.save()