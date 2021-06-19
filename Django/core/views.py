from django.http import request
from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm
# Create your views here.

def registro (request):
    return render(request, 'core/Registro.html')

def registrados (request):
    cliente = Cliente.objects.all()
    datos = {
        'cliente': cliente
    }
    return render(request, 'core/lista_Registrados.html', datos)

def add_Cliente (request):
    datos = {'form': ClienteForm()}
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"

    return render(request, 'core/add_Cliente.html', datos)
