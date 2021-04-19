from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from django.contrib.auth import get_user_model


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        email = sociallogin.user.email.lower().split("@")
        user = User.objects.get(email=sociallogin.user.email)
        if email[1] != "sapalomera.cat":
            raise ImmediateHttpResponse(render(request, "accounts/login.html"))
        if user.groups.all() != 0:
            print("hola")


class MyAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        email = request.user.email
        user = User.objects.get(email=email)
        grups = user.groups.all()
        print(grups)
        print(user)
        print(email)
        if not grups:
            path = "/groups/"
            return path
        else:
            path = "/aplicacions/"
            return path
