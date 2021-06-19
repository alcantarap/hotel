from django.db import models


# Create your models here.

class Cliente(models.Models):
    id_cliente = models.IntegerField(primary_key=True, verbose_name= 'Id Cliente' )
    nombre = models.CharField(max_length= 100, verbose_name = 'Nombre Cliente' )
    apellido = models.CharField(max_length= 100, verbose_name = 'Apellido Cliente' )
    nom_usuario = models.CharField(max_length= 100, verbose_name = 'Nombre Usuario' )
    num_telefonico = models.IntegerField(max_length= 9, verbose_name = 'Numero de Telefono')
    correo = models.EmailField(max_length= 100, verbose_name = 'Correo Electronico')
    contrasena = forms.CharField(label="Password", max_length=50 , widget=forms.PasswordInput, strip=False, verbose_name= 'Contraseña')
    
    def __str__(self):
        return self.nombre
    

