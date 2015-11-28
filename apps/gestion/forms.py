
from django.forms import ModelForm
from django import forms
from .models import *
import datetime

class ClienteForm(forms.ModelForm):
	nombre					= forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required form-control','placeholder':'Indique el nombre del cliente'})))
	fecha_nacimiento 		= forms.DateField(required=False,widget=forms.DateInput(attrs=dict({'class':'required form-control','placeholder':'dd/mm/yyyy'})))
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
		('trailer','TRAILER'),
		('motorhome','MOTORHOME'),
		)
	tipo_vehiculo			= forms.ChoiceField(choices=TIPO_VEHICULO_CHOICES)
	modelo_marca			= forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required form-control','placeholder':'Ingrese la marca y modelo del vehiculo.'})))
	patente 				= forms.CharField(widget=forms.TextInput(attrs=dict({'required':'required','class':'form-control col-md-2','autocomplete':'off','placeholder':'Ingrese el numero de patente.'})))
	observaciones			= forms.CharField(required=False,widget=forms.Textarea(attrs=dict({'class':'requiered form-control','placeholder':'Aqui escriba todo los datos que considere relevantes acerca del vehiculo.'})))

	class Meta:
		model 	= Vehiculo
		exclude = []

class TrabajoForm(forms.ModelForm):
	vehiculo 		= forms.ModelChoiceField(widget=forms.Select(attrs={'size':'13'}), queryset= Vehiculo.objects.all())
	fecha_ingreso	= forms.DateField(initial=datetime.date.today)
	km_ingreso 		= forms.CharField(required = False,widget=forms.TextInput(attrs=dict({'class':'form-control','placeholder':'Si es posible ingrese el kilometraje actual.'})))
	descripcion 	= forms.CharField(required = False,widget=forms.Textarea(attrs=dict({'class':'required form-control','placeholder':'Describa el trabajo realizado.'})))
	precio 			= forms.CharField(required = False,widget=forms.TextInput(attrs=dict({'class':'form-control','disabled':'disabled'})))
	fecha_entrega	= forms.DateField(initial=datetime.date.today,required=False)

	class Meta:
		model  	= Trabajo
		exclude = ['estado',]

