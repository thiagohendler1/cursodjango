from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):   ##primera vista

    p1 = Persona('Profesor Thiago', 'Hendler')

    # nombre = 'Thiago'
    
    # apellido = 'Hendler'

    ahora = datetime.datetime.now()

    
    doc_externo = open("C:/Users/thiag/OneDrive/Escritorio/Thiago/PROGRAMACIÓN/cursodjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    
    plt = Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx = Context({'nombre_persona':p1.nombre, 'apellido_persona': p1.apellido, 'fecha_ahora': ahora})
    
    documento = plt.render(ctx)
    
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse('Chau!')

def dameFecha(request):
    
    fecha_actual = datetime.datetime.now()
    
    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s 
    </h2>
    </body>
    </html>
    """ % fecha_actual
    
    return HttpResponse(documento)

def calculaEdad(request, edad, agno):
    
    #edadActual = 18
    
    periodo = agno - 2023
    edadfutura = edad + periodo
    
    documento = """
    <html>
    <body>
    <h2>
    En el año %s tendrás %s años
    </h2>
    </body>
    </html>
    """ %(agno, edadfutura)
    
    return HttpResponse(documento)