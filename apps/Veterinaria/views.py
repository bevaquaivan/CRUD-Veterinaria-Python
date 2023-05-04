from django.shortcuts import render

def inicio(request):
    return render(request,'inicio.html')

def cliente(request):
    return render(request,'Veterinaria/Cliente/index.html')
