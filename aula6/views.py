# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from aula6.models import Contato
def index(request):
    lista = Contato.objects.all
    if request.method=='POST':
        c=Contato()

        c.first_name=request.POST.get('nome')
        c.last_name = request.POST.get('sobrenome')
        c.email = request.POST.get('email')
        c.twitter= request.POST.get('twitter')
        c.save()

        return render(request, 'aula6/index.html', {'lbl': lista})
    else:
        return render(request, 'aula6/index.html')