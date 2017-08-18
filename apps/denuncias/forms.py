from __future__ import absolute_import
from django.forms import ModelForm, TextInput
from apps.denuncias.models import Denuncia
from django import forms

class DenunciaForm(forms.ModelForm):

	class Meta:
		model = Denuncia
		exclude = ('user', 'fecha', )
		fields = [
			'descripcion',
			'dn_servicio',
			'dn_tiposervicio',
			'lat',
			'lng',
		]
		labels = {
			'dn_servicio': 'Que esta ocurriendo?',
			'dn_tiposervicio': 'Que tipo de servicio?',
			'descripcion': 'Comenta que esta pasando',	 
			'lat': 'Latitud',
			'lng': 'Longitud',

		}
		widgets = {
			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
			'dn_servicio':forms.Select(attrs={'class':'form-control'}),
			'dn_tiposervicio':forms.Select(attrs={'class':'form-control'}),
			'latitud':forms.TextInput(attrs={'class':'form-control'}),
			'longitud':forms.TextInput(attrs={'class':'form-control'}),
		}