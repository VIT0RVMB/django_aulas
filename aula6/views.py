# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# -*- coding:utf-8 -*-
from aula6.models import Contato
from aula6.forms import ContatoForm
from aula6.forms import UpdateForm

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
def index(request):
    contatoForm=ContatoForm()
    lista = Contato.objects.all
    if request.method=='POST':
        contatoForm=ContatoForm(request.POST)
        if contatoForm.is_valid():
            contatoForm.insertContato(None)
            return HttpResponseRedirect(reverse('aula6_index'))






    return render(request, 'aula6/index.html', {'lbl':lista,
                'form':contatoForm})




def detail(request,id):
    contato=get_object_or_404(Contato, id=id) #Procura objeto do tipo Contato, pelo id.
    #Leia: https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#get-object-or-404
    initial={
        'first_name':contato.first_name,
        'last_name':contato.last_name,
        'email': contato.email,
        'twitter': contato.twitter
    } #dicionário initial armazena os dados do objeto Contato, serve para jogar valores iniciais no form
      #Leia: https://docs.djangoproject.com/en/1.10/ref/forms/api/#dynamic-initial-values
    if request.method=='POST':
        form=UpdateForm(request.POST)
        if form.is_valid():

            form.insertContato(contato)
            return HttpResponseRedirect(reverse('aula6_index'))
    else:
        form=ContatoForm(initial)

    return render(request, 'aula6/detail.html', {'contato': contato, 'form':form})


