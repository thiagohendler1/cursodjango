from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
                ##CharField == Para utilizar texto y DEBEMOS PASARLE UN PARÁMETRO

    direccion = models.CharField(max_length=50, verbose_name='La Dirección')
                                #Este último parámetro se utiliza para modificar el nombre con el que aparece en el admin este campo

    email = models.EmailField(blank=True, null=True) ##Con estos dos últimos parámetros hacemos que sea un campo opcional
                ##Con este campo solo se van a poder introducir direcciones de email válidas.
    
    tfno = models.CharField(max_length=7)
    
    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    
    precio = models.IntegerField()
                ##Con este campo solo se van a poder introducir números enteros. 

    def __str__(self):
        return f'El nombre es {self.nombre} - la sección es {self.seccion} - el precio es {self.precio}'
    
class Pedidos(models.Model):
    numero = models.IntegerField()

    fecha = models.DateField()
            ##Con este campo se van a poder introducir fechas. 
    
    entregado = models.BooleanField()
                    ##Con este campo se van a poder ingresar solo True o False.
    
    def __str__(self):
        return f"Número de pedido: {self.numero} - Fecha: {self.fecha} - Entregado: {self.entregado}"