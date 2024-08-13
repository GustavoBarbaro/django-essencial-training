from typing import Any
from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from datetime import datetime

#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import TemplateView
from django.views.generic import CreateView

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


# Create your views here.

#vamos criar uma classe pois o django fica mais facil
#class-based

class LoginInterfaceView (LoginView):
    template_name = 'home/login.html'


class LogoutinInterfaceView (LogoutView):
    template_name = 'home/logout.html'



class SignupView (CreateView, LoginRequiredMixin):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'


    #daria para usar o ligin_url e redirecionar pra outro lugar se fosse o caso de o usuário NÃO estar logado
    #mas como ele está logado: 

    #precisamos dar override no metodo get 
    #para permitir apenas q usuários não logados acessem o signin

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:

        if self.request.user.is_authenticated:
            return redirect('notes.list')

        return super().get(request, *args, **kwargs)



class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    # extra_content = {'today': datetime.today()}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.now()  # Use datetime.now() para obter a data e hora atuais
        return context

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/autorized.html'
    login_url='/admin'


""" 
    def casa (request): 
    #return HttpResponse('Hello, Sr. Stark !')
    return render (request, 'home/welcome.html', {'today': datetime.today()})
      """


""" # esse decorator deve bloquear o acesso de qualquer usuario que não esteja logado
@login_required (login_url='/admin')
def autorize (request):

    return render(request, 'home/autorized.html', {}) 
"""