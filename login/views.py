from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from allauth.account.views import LoginView
from .forms import UsuariAfegirGrup
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

class GoogleLoginView(LoginView):
    template_name = 'accounts/login.html'

def grup_propi(func):
    def comprobar_grup(request, *args, **kwargs):
        pk = kwargs["pk"]
        if pk != request.user.id:
            return HttpResponse('Unauthorized', status=401)
        return func(request, *args, **kwargs)
    return comprobar_grup

@login_required
@grup_propi
def usuari_grup(request, pk):
    usuari = User.objects.get(id=pk)
    if request.method == "POST":
        if(pk != request.user.id):
            return redirect("/aplicacions/")

        form = UsuariAfegirGrup(request.POST)
        if form.is_valid():
            idCurs = form.cleaned_data['Curs']
            grup = Group.objects.get(id=idCurs)
            grup.user_set.add(usuari)
        return redirect("/aplicacions/")
    else:

        form = UsuariAfegirGrup()
        return render(request, 'accounts/grup.html', {'form': UsuariAfegirGrup})
