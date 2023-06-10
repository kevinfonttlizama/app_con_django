from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render





#funcion vista
# primera vista
class Persona():
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido 


def saludo(request):
    # doc_externo=open("C:/Users/kevin/OneDrive/Escritorio/app_con_django/projectone/projectone/templates/index.html")

    temas_del_curso=[
            "Plantillas", #<--- lista dentro de diccionario
            "Modelos",
            "Formularios",
            "Vistas",
            "Modelo"
    ]

    p1=Persona("kevin","fontt")
    ahora=datetime.datetime.now()

    # temp=Template(doc_externo.read())

    # doc_externo.close()



    # context = Context({
    #     "nombre_persona":p1.nombre,
    #     "apellido_persona":p1.apellido,
    #     "hora_actual":ahora,
    #     "temas":temas_del_curso,
    
    # }) diccionario pyrhon con sus respectivos pares clave valor podemos usarlo para pasar valores a la plantilla 

    doc_externo = get_template('index.html')

    document = doc_externo.render({
         "nombre_persona":p1.nombre,
         "apellido_persona":p1.apellido,
         "hora_actual":ahora,
         "temas":temas_del_curso,
    
     })

    return render(request, 'index.html',
        #metodo render para renderizar el documento
        #el contexto es un argumento opcional
    context=({
        "nombre_persona":p1.nombre,
        "apellido_persona":p1.apellido,
        "hora_actual":ahora,
        "temas":temas_del_curso,
    
 }))

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