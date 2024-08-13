from typing import Any, List
from django.http.response import HttpResponseRedirect
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import NotesForm
from .models import Notes

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    login_url = '/admin'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = '/admin'

class NotesCreatedView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = '/admin'

    #precisamos dar override nesse metodo para poder criar nota com FK
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save(commit=False) #injetamos o usuario logado como parte do objeto
        #assim ele cria o objeto mas não salva no BD ainda 

        #então pegamos o usuario de fato aqui
        self.object.user = self.request.user
        self.object.save() # para então salvar no BD
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/login'

    #isso aqui vai pegar a query que vai nos permitir mostrar apenas 
    #as notas criadas pelo usário logado

    #a ideia eh usar o request que o usuário mandar para poder
    #identificar ele e então retornar apenas as suas notas
    def get_queryset(self):
        return self.request.user.notes.all()




class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'



""" 
from django.shortcuts import render
from django.http import Http404

from .models import Notes





# Create your views here.

def list (requests):
    allNotes = Notes.objects.all()
    return render(requests, 'notes/notes_list.html', {'notes': allNotes})


def detail (request, pk):

    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist!")

    return render(request, 'notes/notes_detail.html', {'notes': note}) """