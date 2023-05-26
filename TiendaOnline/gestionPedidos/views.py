from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

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

# def contacto(request):
    
#     if request.method == 'POST':   #Si esto es True significa que hemos pulsado el botón de enviar. 
        
#         subject = request.POST['asunto']  #Nos traemos el asunto del mail
        
#         message = request.POST['mensaje'] + ' ' + request.POST['email']  #Nos traemos el mensaje acompañado del mail por si deseamos contactar a esa persona nuevamente.
        
#         email_from = settings.EMAIL_HOST_USER #Le decimos de donde tiene que venir ese gmail
        
#         recipient_list = ['maildeprueba@prueba.com'] #Especificamos a donde queremos que viaje toda esa información. 
#                             #Aquí ponemos el mail a donde queremos que nos llegue toda la información. 

#         send_mail(subject, message, email_from, recipient_list) #Con esta función mandamos el mail
#         #Argiumentos: Asunto, mensaje, de donde viene el mail, hacia donde va dirigido. 

#         return render(request, 'busqueda_productos.html')
    
#     return render(request, 'contacto.html')

def contacto(request):
    
    if request.method == 'POST':
        
        miformulario = FormularioContacto(request.POST)
                        #Ponemos esto último para que en el formulario venga toda la información introducida por el usuario.
        
        #Luego, hay que preguntarle si es valido o no el formulario y decirle que hacer en cada caso ==
        if miformulario.is_valid():
            
            infForm = miformulario.cleaned_data #Primero limpiamos el form y dejamos solo la información importante.
            
            send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email', ''), ['']) #Con este método pedimos la información del formulario para que la envíe al correo electrónico. 
            #      Rescatamos los campos del formulario.     Aquí envíamos el formulario con el método get()
            
            #Como primer parámetro del método get('ingresamos el mail que el usuario introdujo', 'aquí podriamos poner el mail que configuramos en el archivo setting.py. PUEDE QUEDAR VACÍO ASI COMO ESTÁ Y NO PASA NADA')
            
            #En el último parámetro del método send_mail, entre los [] ponemos el mail a donde tiene que ser enviada toda la información, Es decir, el mail del usuario. 
            
            return render(request, 'busqueda_productos.html')
    
    else:
        
        miformulario = FormularioContacto()  
    
    #Este else sirve para que cuando el usuario ingresa a este form, lo encuentre vacío. Ya que siempre se va a ingresar a este ELSE
    # mientras que el usuario no haya apretado el botón de enviar. 
    
    return render(request, 'formulario_contacto.html', {'form': miformulario})
        #Aquí le decimos que nos renderize este documento, y aquí que nos lo renderize con lo almacenado en esa variable.
                                                        #que en este caso es un formulario vacío. 