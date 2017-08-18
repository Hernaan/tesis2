from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
class Servicio(models.Model):
	servicio = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.servicio



class TipoServicio(models.Model):
	Tipo_Servicio = models.CharField(max_length=100)
	servicio_id = models.ForeignKey(Servicio, null=True, blank=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.Tipo_Servicio



class Denuncia(models.Model):
	descripcion = models.TextField('Descripcion', blank=True, null=True)
	lat = models.CharField('Longitud', max_length=100)
	lng = models.CharField('Latitud', max_length=100)
	fecha = models.DateTimeField('Fecha de creacion', auto_now_add=True)
	user = models.ForeignKey(User, verbose_name='Usuario', related_name='denuncias', default=True)
	dn_servicio = models.ForeignKey(Servicio)
	dn_tiposervicio = models.ForeignKey(TipoServicio)

	def __unicode__(self):
		return self.descripcion