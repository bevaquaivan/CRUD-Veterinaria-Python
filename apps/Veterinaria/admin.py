from django.contrib import admin
from .models import Cliente, TipoMascota, Mascota, HistoriaClinica


# Register your models here.
admin.site.register(Cliente)
admin.site.register(TipoMascota) 

class HistoriaClinica_inline(admin.StackedInline):
    model= HistoriaClinica
    extra=0
    
class Mascota_Admin(admin.ModelAdmin):
    inlines=[
    HistoriaClinica_inline,
    ]
    
admin.site.register(Mascota, Mascota_Admin)