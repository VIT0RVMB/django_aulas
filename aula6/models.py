from django.db import models

# Create your models here.
class Contato(models.Model):
    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=80)
    email=models.EmailField(max_length=100)
    twitter=models.URLField(max_length=100)

    def __unicode__(self):
        return '%s %s' %(self.first_name, self.last_name)