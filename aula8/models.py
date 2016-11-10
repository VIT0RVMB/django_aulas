from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
	"""docstring for ClassName"""
	nome=models.CharField(u'nome',max_length=50)
	birthday=models.DateField(u'birthday', null=False, blank=False)
	bios=models.TextField(u'bios', )




	def __init__(self, nome):
		
		nome=self.nome


	def __unicode__(self):
		return self.nome

		
		
class UserPlus(User):
	bios=models.TextField(u'bios')

	def __unicode__(self):
		return self.name