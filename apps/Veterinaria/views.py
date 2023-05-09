from django.views.generic import View
from django.shortcuts import render
from apps.Veterinaria.forms import *
from apps.Veterinaria.models import *


def home(request):
    return render(request, 'index.html',)

def cliente(request):
    return render(request,'Cliente/index.html')

def editarcliente(request, id):
    cliente = Cliente.objects.get(pk=id)
    form=CreateClientForm(request.POST or None, instance=cliente)
    return render(request, 'Cliente/form.html', {'form': form})
