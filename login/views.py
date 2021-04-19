from django.shortcuts import render

from allauth.account.views import LoginView, LogoutView


class GoogleLoginView(LoginView):
    template_name = 'accounts/login.html'


class GoogleLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
