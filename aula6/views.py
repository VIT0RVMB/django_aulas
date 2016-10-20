# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from aula6.models import Contato
from aula6.forms import ContatoForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
def index(request):
    contatoForm=ContatoForm()
    lista = Contato.objects.all
    if request.method=='POST':
        contatoForm=ContatoForm(request.POST)
        if contatoForm.is_valid():
            contatoForm.insertContato()
            return HttpResponseRedirect(reverse('aula6_index'))






    return render(request, 'aula6/index.html', {'lbl':lista,
                'form':contatoForm})