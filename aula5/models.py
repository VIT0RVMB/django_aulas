#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Contato(models.Model):
    nome=models.CharField(max_length=130)
    email=models.EmailField()
    twitter=models.URLField(verify_exists='false')
    data_nascimento=models.DateField()

    def __unicode__(self):
        return self.nome


class Categoria(models.Model):
    nome=models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome


class Post(models.Model):
    titulo=models.CharField(max_length=100)
    texto=models.CharField(max_length=800)
    categoria=models.ManyToManyField(Categoria)

    def __unicode__(self):
        return self.titulo


class Comentarios(models.Model):
    autor=models.CharField(max_length=100)
    comentario=models.CharField(max_length=240)
    post=models.ForeignKey(Post)
    def __unicode__(self):
        return self.autor

