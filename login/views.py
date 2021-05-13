from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.models import User
from allauth.account.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Curs,Group
class GoogleLoginView(LoginView):
    template_name = 'login/login.html'

@login_required
def usuari_grup(request):
    if request.method == 'POST':
        grup = Group.objects.get(id=request.POST.get('grup'))
        grup.user_set.add(request.user)
        return JsonResponse({'success': True}, status=201)
    else:
        llista_cursos = Curs.objects.exclude(nom="Professors")
        return render(request, 'login/grup.html', {'llista_cursos': llista_cursos})

def get_json_grups_data(request, *args, **kwargs):
    selected_curs = kwargs.get('curs_id')
    obj_grup = list(Group.objects.filter(curs=selected_curs).values("id","name"))
    return JsonResponse({'data':obj_grup})