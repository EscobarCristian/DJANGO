from django.db import models

# Create your models here.
class Persona(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=60)
	apellido = models.CharField(max_length=100,null=True)
	club = models.CharField(max_length=50,null=True)
	email = models.CharField(max_length=50,null=True)
	dni = models.CharField(max_length=8,null=True)

class Meta:
	verbose_name = ('Persona')
	verbose_name_plural = ('Personas')

def __str__(self):
	  return self.nombre