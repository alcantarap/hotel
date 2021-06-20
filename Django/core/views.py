from django.http import request
from django.shortcuts import redirect, render
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

def add_cliente (request):
    datos = {'form': ClienteForm()}
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"

    return render(request, 'core/add_Cliente.html', datos)


def edit_cliente (request, pk):
    cliente = Cliente.objects.get(id_cliente=pk)

    if request.method =='POST':
        formulario_edit = ClienteForm(data=request.POST, instance=cliente)
        if formulario_edit.is_valid:
            formulario_edit.save()
            return redirect(to="registrados")
    
    else:
        datos = {
            'form':ClienteForm(instance=cliente)
        }
        return render(request, 'core/edit_Cliente.html', datos)


def delete_cliente(request, pk):
    cliente = Cliente.objects.get(id_cliente=pk)
    cliente.delete()
    return redirect(to="registrados")








    
