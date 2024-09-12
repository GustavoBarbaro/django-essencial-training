from django import forms
from django.core.exceptions import ValidationError

from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = {'title', 'text'}
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text' : forms.Textarea(attrs={'class': 'form-control my-5'}),
        }
        labels = {
            'title': 'Título da Nota',
            'text': 'Texto da nota',
        }

    # def clean_title(self):
    #     title = self.cleaned_data['title']

    #     #agora vamos fazer o filtro
    #     #para apenas aceitar palavras com django no nome
    #     #util para e-mails pois possuim validação forte

    #     if 'Django' not in title:
    #         raise ValidationError("Apenas Aceitamos notas com Django no Titulo")
    #     return title