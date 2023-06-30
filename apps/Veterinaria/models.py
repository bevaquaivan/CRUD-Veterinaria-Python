from django.db import models

# Create your models here.
class Cliente(models.Model):
    dni = models.IntegerField(verbose_name="DNI", unique=True,)
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    apellido = models.CharField(max_length=255, verbose_name="Apellido", )
    ciudad = models.CharField(max_length=255, verbose_name="Ciudad", null=True )
    nombre_calle = models.CharField(max_length=255, verbose_name="Nombre de la Calle",)
    numero_calle = models.IntegerField(verbose_name='Número de la calle',null=True)
    telefono = models.IntegerField(verbose_name="Número de teléfono",)
    fecha_de_alta = models.DateField(verbose_name="Fecha de Alta", blank=False,)
    estado = models.BooleanField(verbose_name="Estado")
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        ordering = ['id']
        db_table = 'Cliente'
        verbose_name_plural = 'clientes'
        verbose_name = 'cliente'
        
        
# CLASE MASCOTA #

class TipoMascota(models.Model):
    nombretipo = models.CharField(max_length=255, verbose_name="Tipo de Mascota")
    
    class Meta:
        ordering = ['id']
        db_table = 'TipoMascota'
        verbose_name_plural = 'tipo mascotas'
        verbose_name = 'tipo mascota'
        
    def __str__(self):
        return f"{self.nombretipo}"

class Mascota(models.Model):
    propietario = models.ForeignKey(Cliente, verbose_name='Propietario',on_delete=models.PROTECT )
    numero_chip = models.IntegerField(verbose_name='Número de chip', blank=True,)
    nombre_mascota = models.CharField(verbose_name='Nombre de la Mascota', max_length=255,)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    tipo_mascota = models.ForeignKey(TipoMascota,verbose_name='Tipo de Mascota', on_delete=models.PROTECT,)
    color = models.CharField(verbose_name='Color de la Mascota', max_length=100, null=True)
    estado = models.BooleanField(verbose_name="Estado")

    
    def __str__(self):
        return f"{self.nombre_mascota} {self.propietario}"
    
    class Meta:
        ordering = ['id']
        db_table = 'Mascota'
        verbose_name_plural = 'mascotas'
        verbose_name = 'mascota'
        
class HistoriaClinica(models.Model):
    mascota = models.ForeignKey(Mascota, verbose_name='Mascota',on_delete=models.PROTECT)
    fecha_consulta = models.DateField(verbose_name='Fecha de consulta')
    observaciones = models.CharField(verbose_name='Observaciones Realizadas', max_length=400)
    
    def __str__(self):
        return f"{self.mascota}" 