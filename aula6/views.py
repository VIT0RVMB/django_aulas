# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from aula6.models import Contato
from aula6.forms import ContatoForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
def index(request):
    c = Contato()
    lista = Contato.objects.all
    if request.method=='POST':
        contatoForm=ContatoForm(request.POST)
        if contatoForm.is_valid():
            c.first_name=contatoForm.cleaned_data['nome']
            c.last_name = contatoForm.cleaned_data['sobrenome']
            c.email = contatoForm.cleaned_data['email']
            c.twitter= contatoForm.cleaned_data['twitter']
            c.save()
            return HttpResponseRedirect(reverse('aula6/index.html'))

    else:
        contatoForm=ContatoForm



    return render(request, 'aula6/index.html', {'lbl':lista,
                'form':contatoForm})