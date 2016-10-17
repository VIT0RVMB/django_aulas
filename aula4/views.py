# Create your views here.
# -*- coding:utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse
from aula5.models import Contato
from django.views.decorators.csrf import csrf_exempt
from datetime import date
@csrf_exempt
def index(request):
	if request.method=='POST':
		contato=Contato()
		contato.nome=str(request.POST.get('nome'))
		contato.email = str(request.POST.get('email'))
		contato.twitter= str(request.POST.get('twitter'))
		contato.data_nascimento=date(1994,4,1)
		contato.save()
		return HttpResponse('<h3>Cadastro Realizado!</h3>')
	else:
		return render(request, 'aula4/index.html')





