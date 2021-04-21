from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        email = sociallogin.user.email.lower().split("@")
        if email[1] != "sapalomera.cat":
            raise ImmediateHttpResponse(render(request, "accounts/login.html"))


class MyAccountAdapter(DefaultAccountAdapter):

    def get_signup_redirect_url(self, request):
        print(self)
        print(request)
        return resolve_url("/grups/")

    def get_login_redirect_url(self, request):
        email = request.user.email
        user = User.objects.get(email=email)
        grups = user.groups.all()
        if not grups:
            path = "/grups/"
            return path
        else:
            path = "/aplicacions/"
            return path
