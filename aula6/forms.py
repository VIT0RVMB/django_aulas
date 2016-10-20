from django import forms
from aula6.models import Contato

class ContatoForm(forms.Form):
    first_name=forms.CharField(label='nome', max_length=60)
    last_name=forms.CharField(label='sobrenome', max_length=80)
    email=forms.EmailField(label='email',max_length=100)
    twitter=forms.URLField(label='twitter', max_length=100)



    def insertContato(self):
        c=Contato()
        c.first_name = self.cleaned_data['first_name']
        c.last_name = self.cleaned_data['last_name']
        c.email = self.cleaned_data['email']
        c.twitter = self.cleaned_data['twitter']
        c.save()




