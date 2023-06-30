from django.views.generic import View
from django.shortcuts import render
from apps.Veterinaria.forms import *
from apps.Veterinaria.models import *


def home(request):
    return render(request, 'index.html',)

def cliente(request):
    return render(request,'Cliente/index.html')

# CLIENTE #

def editarcliente(request, id):
    cliente = Cliente.objects.get(pk=id)
    form=CreateClientForm(request.POST or None, instance=cliente)
    return render(request, 'Cliente/form.html', {'form': form})

# MASCOTA #

def editarmascota(request, id):
    mascota = Mascota.objects.get(pk=id)
    form=CreateMascotaForm(request.POST or None, instance=mascota)
    return render(request,  'Mascota/form.html', {'form': form})

# HISTORIA CLINICA #

def editarhistoriaclinica(request, id):
    historiaclinica = HistoriaClinica.objects.get(pk=id)
    form=CreateHistoriaClinica(request.POST or None, instance=historiaclinica)
    return render(request,'HistoriaClinica/form.html', {'form': form})