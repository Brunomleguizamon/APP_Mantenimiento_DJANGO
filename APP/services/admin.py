from django.contrib import admin
from .models import requests, CRM

@admin.register(requests)
class RequestAdmin(admin.ModelAdmin):
    list_display=('id_equipo', 'equipo', 'CRM', 'fecha_creacion', 'detalle', 'solicitante', 'area', 'sector', 'responsable_seguimiento')
    list_filter=('id_equipo', 'equipo', 'CRM', 'fecha_creacion', 'detalle', 'solicitante', 'area', 'sector', 'responsable_seguimiento')


@admin.register(CRM)
class CRMAdmin(admin.ModelAdmin):
    list_display=('area', 'requerimiento', 'descripcion', 'prioridad')
    list_filter=('area', 'requerimiento', 'descripcion', 'prioridad')