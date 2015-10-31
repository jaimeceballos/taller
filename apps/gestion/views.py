from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.core import serializers
from django.http import HttpResponse,HttpResponseRedirect, HttpResponse,Http404
from django.core.urlresolvers import reverse
from django.db import transaction
import time
from .forms import *
from .models import *

# Create your views here.
def home(request):
	vehiculo 	= VehiculoForm()
	cliente 	= ClienteForm()
	values={
		'vehiculo' : vehiculo,
		'cliente'  : cliente,
	}
	return render_to_response('index.html',values,context_instance = RequestContext(request))

def nuevo_vehiculo(request):
	vehiculo 	= VehiculoForm()
	cliente 	= ClienteForm()
	values={
		'vehiculo' : vehiculo,
		'cliente'  : cliente,
	}
	return render_to_response('gestion/nuevo_vehiculo.html',values,context_instance = RequestContext(request))
def guardar_vehiculo(request):
	print request.method
	if request.method == "POST":
		vehiculo = VehiculoForm(request.POST)
		cliente = ClienteForm(request.POST)
		print vehiculo.errors #and cliente.is_valid() 
		if vehiculo.is_valid() and cliente.is_valid():
			auto = Vehiculo()
			auto.patente 		= vehiculo.cleaned_data['patente']
			auto.tipo_vehiculo  = vehiculo.cleaned_data['tipo_vehiculo']
			auto.modelo_marca	= vehiculo.cleaned_data['modelo_marca']
			auto.observaciones	= vehiculo.cleaned_data['observaciones']
			persona = Cliente()
			persona.nombre 			= cliente.cleaned_data['nombre']
			persona.telefono_numero	= cliente.cleaned_data['telefono_numero']
			persona.direccion 		= cliente.cleaned_data['direccion']
			persona.otro_contacto	= cliente.cleaned_data['otro_contacto']
			try:
				persona.save()
				auto.save()
				cliente_vehiculo  = ClienteVehiculo()
				cliente_vehiculo.vehiculo 	= auto
				cliente_vehiculo.cliente 	= persona
				cliente_vehiculo.fecha 		=  time.strftime("%Y-%m-%d")
				cliente_vehiculo.save()
			except:
				error = 'No se pudo guadar.'
				vehiculo 	= VehiculoForm()
				cliente 	= ClienteForm()
				values={
					'error' : error,
					'vehiculo' : vehiculo,
					'cliente'  : cliente,
				}
				return render_to_response('index.html',values,context_instance = RequestContext(request))				
			finally:
				return HttpResponseRedirect(reverse("home"))
	return HttpResponseRedirect(reverse("home"))	

def obtener_vehiculo(request,patente):
	data 		= request.POST
	vehiculo 	= Vehiculo.objects.filter(patente = patente)
	data = serializers.serialize("json", vehiculo)
	return HttpResponse(data, content_type='application/json')

def cargar_trabajo(request):
	trabajo = TrabajoForm()

	values = {
		'trabajo' : trabajo,
	}
	return render_to_response('gestion/trabajo.html',values,context_instance = RequestContext(request))				

def cargar_trabajo_save(request):
	if request.method == "POST":
		trabajo 	= TrabajoForm(request.POST)
		if trabajo.is_valid():
			nuevo 				= Trabajo()
			nuevo.vehiculo 		= trabajo.cleaned_data['vehiculo']
			nuevo.fecha_ingreso = time.strftime("%Y-%m-%d")
			nuevo.km_ingreso 	= trabajo.cleaned_data['km_ingreso']
			nuevo.descripcion	= trabajo.cleaned_data['descripcion']
			nuevo.estado 		= 1
			nuevo.save()
			values = {
				'error' : 'Trabajo guardado correctamente.',
				'trabajo' : TrabajoForm()
			}
			return render_to_response('gestion/trabajo.html',values,context_instance = RequestContext(request))
	print trabajo.errors
	values = {
		'error' : 'No se pudo realizar la operacion, vuelva a intentarlo.',
		'trabajo' : TrabajoForm()
	}
	return render_to_response('gestion/trabajo.html',values,context_instance = RequestContext(request))

def ver_trabajos(request):
	listado 	= Trabajo.objects.filter(estado=1).order_by('-id')
	values = {
		'listado':listado,
	}
	return render_to_response('gestion/ver_trabajos.html',values,context_instance = RequestContext(request))

def finalizar_trabajo(request,id):
	form 		 	= TrabajoForm(instance=Trabajo.objects.get(id=id))
	trabajo 		= Trabajo.objects.get(id=id)
	cliente 		= trabajo.vehiculo.pertenece_a.get(fecha_hasta=None).cliente
	values = {
		'cliente' 	: cliente,
		'form' 		: form,
		'trabajo' 	: trabajo,
	}
	return render_to_response('gestion/finalizar_trabajo.html',values,context_instance = RequestContext(request))

def finaliza(request,id):
	if request.method == "POST":
		form = TrabajoForm(request.POST)
		print form.as_p()
		if form.is_valid():
			trabajo 				= Trabajo.objects.get(id=id)
			trabajo.descripcion 	= form.cleaned_data['descripcion']
			trabajo.precio 			= form.cleaned_data['precio']
			trabajo.fecha_entrega 	= time.strftime("%Y-%m-%d")
			trabajo.estado 			= 2
			trabajo.save()
			return HttpResponseRedirect(reverse('ver_trabajos'))

	form 		 	= TrabajoForm(instance=Trabajo.objects.get(id=id))
	trabajo 		= Trabajo.objects.get(id=id)
	cliente 		= trabajo.vehiculo.pertenece_a.get(fecha_hasta=None).cliente
	values = {
		'cliente' 	: cliente,
		'form' 		: form,
		'trabajo' 	: trabajo,
		'error' : 'No se pudo procesar la solicitud.',
	}
	return render_to_response('gestion/finalizar_trabajo.html',values,context_instance = RequestContext(request))

def ver_ultimos_entregados(request):
	listado = Trabajo.objects.filter(fecha_entrega__isnull=False)[:10]
	values = {
		'listado' : listado,
	}
	return render_to_response('gestion/ver_ultimos_entregados.html',values,context_instance = RequestContext(request))

def ver_clientes(request):
	listado 	= Cliente.objects.all()
	values = {
		'listado' : listado,
 	}
 	return render_to_response('gestion/ver_clientes.html',values,context_instance = RequestContext(request))

def ver_vehiculos_cliente(request,id):
	cliente 	= Cliente.objects.get(id=id)
	vehiculos 	= cliente.tiene.all()
	print vehiculos
	values = {
		'cliente' 	: cliente,
		'vehiculos'	: vehiculos,
	}
	return render_to_response('gestion/vehiculos_cliente.html',values,context_instance = RequestContext(request))

def detalle_trabajo(request,id):
	form 		 	= TrabajoForm(instance=Trabajo.objects.get(id=id))
	trabajo 		= Trabajo.objects.get(id=id)
	cliente 		= trabajo.vehiculo.pertenece_a.get(fecha_hasta=None).cliente
	values = {
		'cliente' 	: cliente,
		'form' 		: form,
		'trabajo' 	: trabajo,
	}
	return render_to_response('gestion/ver_detalle_trabajo.html',values,context_instance = RequestContext(request))
