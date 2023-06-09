from django.http import HttpResponse
import datetime
from django.template import Template, Context




#funcion vista
# primera vista 


def saludo(request):
    doc_externo=open("C:/Users/kevin/OneDrive/Escritorio/app_con_django/projectone/projectone/templates/index.html")

    temp=Template(doc_externo.read())

    doc_externo.close()

    context = Context()

    document = temp.render(context)

    return HttpResponse(document)

#debemos entregarle una url a python de esta vista para que cuando naveguemos por esa url podamos acceder a esta vista


def despedida(request):
    return HttpResponse("Hasta luego amigos esto es una despedida de ejemplo")


def obtenerFecha(request):
    fecha_actual= datetime.datetime.now()
    
    document="""<html>
    <body>
    <h1>
    fecha y hora actuales %s
    </h1>
    </body>
        </html>""" %fecha_actual

    return HttpResponse(document)



def calculaEdad(request, edad ,year):
    periodo= year - 2023
    edadFutura = edad + periodo
    document="""<html>
    <body>
    <h2>
    En el año %s tendras %s años
    </h2>
    </body>
        </html>""" %(year,edadFutura)
    

    return HttpResponse(document)