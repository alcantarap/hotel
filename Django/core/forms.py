from django import forms
from django .forms import ModelForm
from .models import Cliente


class ClienteForm (ModelForm):
    class Meta:
        model = Cliente
        fields= ['id_cliente', 'nombre', 'apellido', 'nom_usuario', 'num_telefonico', 'correo', 'contrasena'] 

