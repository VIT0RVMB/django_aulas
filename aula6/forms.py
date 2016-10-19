from django import forms


class ContatoForm(forms.Form):
    first_name=forms.CharField(label='nome', max_length=60)
    last_name=forms.CharField(label='sobrenome', max_length=80)
    email=forms.EmailField(label='email',max_length=100)
    twitter=forms.URLField(label='twitter', max_length=100)