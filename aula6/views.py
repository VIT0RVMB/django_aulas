# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from aula6.models import Contato
def index(request):
    c = Contato()
    lista = Contato.objects.all
    if request.method=='POST':


        c.first_name=request.POST.get('nome')
        c.last_name = request.POST.get('sobrenome')
        c.email = request.POST.get('email')
        c.twitter= request.POST.get('twitter')
        c.save()


    else:


        return HttpResponse(render(request, 'aula6/index.html'))

    return render(request, 'aula6/index.html', {'lbl':lista})