from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.

def busqueda_productos(request):

    return render (request, 'busqueda_productos.html')

def buscar(request):
    
    if request.GET["prd"]:

        #mensaje = 'Articulo buscado: %r' %request.GET['prd']
        producto = request.GET["prd"]  
        
        articulos = Articulos.objects.filter(nombre__icontains=producto)
                                #Funciona como la funcion LIKE en sql (el __icontains)
                                #Busca en el campo nombre la palabra que esta almacenada en producto. 
        #Una vez que ya tenemos el articulo que buscamos cargado, debemos
        #crear un html para que nos muestre esta información en pantalla. 
        
        return render(request, 'resultados_busqueda.html', {'articulos': articulos, 'query': producto})
        
    else:
        
        mensaje = 'No has introducido nada.'

    return HttpResponse(mensaje) 