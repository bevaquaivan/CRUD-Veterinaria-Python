from django import forms

from . models import Cliente
from . models import Mascota
from . models import HistoriaClinica

# CLIENTE #

class CreateClientForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=('__all__')
        
# TIPO MASCOTA #

class CreateMascotaForm(forms.ModelForm):
    class Meta:
        model=Mascota
        fields=('__all__')
        
# HISTORIA CLINICA#

class CreateHistoriaClinica(forms.ModelForm):
    class Meta:
        model=HistoriaClinica
        fields=('__all__')