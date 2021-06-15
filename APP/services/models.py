from django.db import models
from django.db.models.fields.related import OneToOneField
from django.utils import timezone
from django.contrib.auth.models import User


class requests (models.Model):
    
    STATUS_AREA = (
        ('infra','Infraestructura'),
        ('SS','Subsuelo')
    )

    STATUS_SECTOR = (
        ('mante','Mantenimiento'),
        ('bunker','Bunker')
    )
    
    id_equipo = models.CharField(max_length=250) 
    equipo = models.CharField(max_length=250)
    CRM = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField (default=timezone.now)
    detalle= models.TextField()
    solicitante= models.CharField(max_length=250)
    area=models.CharField(max_length=100,
                            choices=STATUS_AREA,
                            default='infra')
    sector=models.CharField(max_length=100,
                            choices=STATUS_SECTOR,
                            default='mante')
    responsable_seguimiento= models.ForeignKey(User,
                                                on_delete=models.CASCADE)
    observaciones= models.TextField()


class CRM (models.Model):

    STATUS_AREA = (
        ('binomio', 'Binomio'),
        ('bioingeniria', 'Bioingenieria'),
        ('centroQuirurgico', 'Centro Quirurgico'),
        ('ConsExternos-Imagenes-Hemodinamia', 'Cons Externos Imagenes-Hemodinamia')
    )

    STATUS_REQUERIMIENTO = (
        ('bioingenieria', 'Reparacion Bioingenieria'),
        ('edilicio', 'Reparacion Edilicio')
    )

    STATUS_PRIORIDAD = (
        ('alta', 'Alta'),
        ('baja', 'Baja'), 
    )

    area = models.CharField(max_length=250,
                            choices=STATUS_AREA,
                            default='bioingenieria')
    requerimiento = models.CharField(max_length=250,
                                    choices=STATUS_REQUERIMIENTO,
                                    default='edilicio')
    descripcion= models.TextField()
    prioridad= models.CharField(max_length=100,
                                choices=STATUS_PRIORIDAD,
                                default='baja')
    creado_by= models.ForeignKey(User,
                                on_delete=models.CASCADE)
    