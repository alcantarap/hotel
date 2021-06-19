from django.db import models


# Create your models here.

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, verbose_name= 'Id Cliente' )
    nombre = models.CharField(max_length= 100, verbose_name = 'Nombre Cliente' )
    apellido = models.CharField(max_length= 100, verbose_name = 'Apellido Cliente' )
    nom_usuario = models.CharField(max_length= 100, verbose_name = 'Nombre Usuario' )
    num_telefonico = models.IntegerField(verbose_name = 'Numero de Telefono')
    correo = models.EmailField(max_length= 100, verbose_name = 'Correo Electronico')
    contrasena = models.CharField( max_length=50 ,  verbose_name= 'Contraseña')
    
    def __str__(self):
        return self.nombre
    

