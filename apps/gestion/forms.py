
from django.forms import ModelForm
from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
	nombre					= forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required form-control','placeholder':'Indique el nombre del cliente'})))
	telefono_numero			= forms.CharField(required=False,widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level','placeholder':'ej:154123456'})))
	direccion				= forms.CharField(required=False,widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level','placeholder':'Indique la direccion del cliente.'})))
	otro_contacto			= forms.CharField(required=False,widget=forms.Textarea(attrs=dict({'class':'form-control','placeholder':'En este campo agregue todos los datos extra que pueda del cliente.'})))

	class Meta:
		model 	= Cliente
		exclude = []

class VehiculoForm(forms.ModelForm):
	TIPO_VEHICULO_CHOICES = (
		('auto','AUTO'),
		('camioneta','CAMIONETA'),
		('camion','CAMION'),
		('moto','MOTO'),
		)
	tipo_vehiculo			= forms.ChoiceField(choices=TIPO_VEHICULO_CHOICES)
	modelo_marca			= forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required form-control','placeholder':'Ingrese la marca y modelo del vehiculo.'})))
	patente 				= forms.CharField(widget=forms.TextInput(attrs=dict({'class':'requiered form-control col-md-2','placeholder':'Ingrese el numero de patente.'})))
	observaciones			= forms.CharField(required=False,widget=forms.Textarea(attrs=dict({'class':'requiered form-control','placeholder':'Aqui escriba todo los datos que considere relevantes acerca del vehiculo.'})))

	class Meta:
		model 	= Vehiculo
		exclude = []

class TrabajoForm(forms.ModelForm):
	vehiculo 		= forms.ModelChoiceField(widget=forms.Select(attrs={'size':'13'}), queryset= Vehiculo.objects.all())
	km_ingreso 		= forms.CharField(required = False,widget=forms.TextInput(attrs=dict({'class':'form-control','placeholder':'Si es posible ingrese el kilometraje actual.'})))
	descripcion 	= forms.CharField(required = False,widget=forms.Textarea(attrs=dict({'class':'required form-control','placeholder':'Describa el trabajo realizado.'})))
	precio 			= forms.CharField(required = False,widget=forms.TextInput(attrs=dict({'class':'form-control','disabled':'disabled'})))

	class Meta:
		model  	= Trabajo
		exclude = ['fecha_ingreso','fecha_entrega','estado',]
