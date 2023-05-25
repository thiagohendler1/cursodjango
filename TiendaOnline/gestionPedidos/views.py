from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def busqueda_productos(request):

    return render (request, 'busqueda_productos.html')

def buscar(request):
    
    if request.GET["prd"]:

        #mensaje = 'Articulo buscado: %r' %request.GET['prd']
        producto = request.GET["prd"]  
        
        if len(producto)>20:
            mensaje='texto demasiado largo'
        
        else:
        
            articulos = Articulos.objects.filter(nombre__icontains=producto)
                                #Funciona como la funcion LIKE en sql (el __icontains)
                                #Busca en el campo nombre la palabra que esta almacenada en producto. 
        #Una vez que ya tenemos el articulo que buscamos cargado, debemos
        #crear un html para que nos muestre esta información en pantalla. 
        
            return render(request, 'resultados_busqueda.html', {'articulos': articulos, 'query': producto})
        
    else:
        
        mensaje = 'No has introducido nada.'

    return HttpResponse(mensaje) 

def contacto(request):
    
    if request.method == 'POST':   #Si esto es True significa que hemos pulsado el botón de enviar. 
        
        subject = request.POST['asunto']  #Nos traemos el asunto del mail
        
        message = request.POST['mensaje'] + ' ' + request.POST['email']  #Nos traemos el mensaje acompañado del mail por si deseamos contactar a esa persona nuevamente.
        
        email_from = settings.EMAIL_HOST_USER #Le decimos de donde tiene que venir ese gmail
        
        recipient_list = ['maildeprueba@prueba.com'] #Especificamos a donde queremos que viaje toda esa información. 
                            #Aquí ponemos el mail a donde queremos que nos llegue toda la información. 

        send_mail(subject, message, email_from, recipient_list) #Con esta función mandamos el mail
        #Argiumentos: Asunto, mensaje, de donde viene el mail, hacia donde va dirigido. 

        return render(request, 'busqueda_productos.html')
    
    return render(request, 'contacto.html')