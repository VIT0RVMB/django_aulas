# -*- coding: utf-8 -*-
from django import forms
from aula6.models import Contato

class ContatoForm(forms.Form):
    #email_errors e default_errors são dicionários criados com o texto das validações padrão.
    #o dicionário é passado no parametro error_messages no método CharField do forms.
    #É só pra alterar o texto das validações padroes mesmo que são em ingles.
    email_errors = {
    'required': 'E-mail obrigatório',
    'invalid': 'Insira um e-mail válido'
    }
    default_errors= {
    'required':'Este campo é obrigatório.',
    'invalid':'Dados invalidos'
    }

    first_name=forms.CharField(error_messages=default_errors, label='nome', max_length=60)
    last_name=forms.CharField(error_messages=default_errors, label='sobrenome', max_length=80)
    email=forms.EmailField(error_messages=email_errors, label='email',max_length=100)
    twitter=forms.URLField(error_messages=default_errors,label='twitter', max_length=100)



    def insertContato(self, c=None):
        
        if c:
            c.first_name = self.cleaned_data['first_name']
            c.last_name = self.cleaned_data['last_name']
            c.email = self.cleaned_data['email']
            c.twitter = self.cleaned_data['twitter']
            c.save()
        else:
            new_c=Contato(
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email'],
                twitter=self.cleaned_data['twitter']
            )
            new_c.save()

    #Este método insere uma validação adicional ao campo email.
    #a variavel 'email' recebe o dado vindo do form e a confição
    #valida se já existe um email igual no banco de dados. 
    #Se for igual a algum e-mail da lista é retornado o erro;
    #Se nao for é retornado o erro.

    def clean_email(self):
        email=self.cleaned_data['email']
        if Contato.objects.filter(email=email):

            raise forms.ValidationError(u'E-mail já cadastrado.')      
         
        return email


class UpdateForm(ContatoForm):
    def clean_email(self):
        email='B0FEZudsnmIV'
        
        if Contato.objects.filter(email=email):

            raise forms.ValidationError(u'E-mail já cadastrado.')      
        
        email=self.cleaned_data['email'] 
        return email


