from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
	url(r'^nuevo_vehiculo/$',nuevo_vehiculo,name='nuevo_vehiculo'),
    url(r'^obtener_vehiculo/(?P<patente>\w+)/$', obtener_vehiculo, name='obtener_vehiculo'),
    url(r'^guardar_vehiculo/$',guardar_vehiculo,name='guardar_vehiculo'),
    url(r'^cargar_trabajo/(?P<id>[0-9]+)/$',carga_trabajo,name='carga_trabajo'),
    url(r'^cargar_trabajo/$',cargar_trabajo,name='cargar_trabajo'),
    url(r'^cargar_trabajo_save/$',cargar_trabajo_save,name='cargar_trabajo_save'),
    url(r'^ver_trabajos/$',ver_trabajos,name='ver_trabajos'),
    url(r'^ver_trabajos_vehiculo/(?P<id>[0-9]+)/$',ver_trabajos_vehiculo,name='ver_trabajos_vehiculo'),
    url(r'^finalizar_trabajo/(?P<id>[0-9]+)/$',finalizar_trabajo,name='finalizar_trabajo'),
    url(r'^finaliza/(?P<id>[0-9]+)/$',finaliza,name='finaliza'),
    url(r'^ver_ultimos_entregados/$',ver_ultimos_entregados,name='ver_ultimos_entregados'),
    url(r'^ver_clientes/$',ver_clientes,name='ver_clientes'),
    url(r'^ver_vehiculos_cliente/(?P<id>[0-9]+)/$',ver_vehiculos_cliente,name='ver_vehiculos_cliente'),
    url(r'^detalle_trabajo/(?P<id>[0-9]+)/$',detalle_trabajo,name='detalle_trabajo'),
    url(r'^imprimir_trabajo/(?P<id>[0-9]+)/$',imprimir_trabajo,name='imprimir_trabajo'),
    url(r'^imprimir_historia/(?P<id>[0-9]+)/$',imprimir_historia,name='imprimir_historia'),
   
]