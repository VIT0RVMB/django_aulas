#-*- coding:utf-8 -*-

Cola de Comandos do Django.

Usuários, Permissões e Grupos:

Imports:

from django.contrib.auth.models import User, Permissions, Group



usuario=User.objects.get(id=1) #recebe usuario de id igual a 1 do banco

usuario.user_permissions.all() #Mostra lista de permissões do usuario em questão;

permissao=Permissions.objects.all() #joga todas as permissões do sistema na instancia;

grupo=Group()
grupo.name('MeuGrupo1')
grupo.save()

ou grupo=Group.create(name='MeuGrupo1')

grupo.permissions.add(permissiao[3]) #adiciona permissão na ocorrencia 3 da lista de permissões;


user.groups.add(grupo) #adiciona usuário no grupo "MeuGrupo1";



