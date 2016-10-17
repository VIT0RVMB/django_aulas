# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse

@csrf_exempt
def index(request):
    if request.method=='POST':
        nome =request.POST.get('name', u'não tem nome')
        return HttpResponse('O nome é: '+ str(nome))
    else:
        formulario='''
            <link href="/statis/css/bootstrap.min.css" rel="stylesheet">
            <form method="post">
                <label>Nome:</label>
                <input name="name" type=text></input>
                <button class="btn btn-default" type=submit>Enviar</button>
            </form>

        '''
        return HttpResponse(formulario)
        
def getMetodo(request):
    metodo= request.method
    return HttpResponse(metodo)
       

def detail(request, id):
    id=calcula(int(id))
    return HttpResponse(u'<h1>Fatorial: %s' %id+'</h1>')


def calcula(num):
    for i in range(1,(num-1)):
        num += num*i
    return num

@csrf_exempt
def fatorial(request):
    if request.method=='POST':
            a=request.POST.get('num', u'Sem número')
            num=calcula(int(a))
            return HttpResponse('Fatorial do número inserido: ' +str(num))
    else:
        formulario='''
                <form method="Post">
                    <label>NÚMERO:</label>
                    <input name="num" type=number/>
                    <button type=submit>Calcular</button>
                </form>

                '''
        return HttpResponse(formulario)






