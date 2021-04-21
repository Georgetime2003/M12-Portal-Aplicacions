from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from allauth.account.views import LoginView, LogoutView
from .forms import UsuariAfegirGrup


class GoogleLoginView(LoginView):
    template_name = 'accounts/login.html'


class GoogleLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


def usuari_grup(request, pk):
    usuari = User.objects.get(id=pk)
    if request.method == "POST":
        form = UsuariAfegirGrup(request.POST)
        if form.is_valid():
            idCurs = form.cleaned_data['Curs']
            grup = Group.objects.get(id=idCurs)
            grup.user_set.add(usuari)
        return redirect("/")
    else:
        form = UsuariAfegirGrup()
        return render(request, 'accounts/grup.html', {'form': UsuariAfegirGrup})
