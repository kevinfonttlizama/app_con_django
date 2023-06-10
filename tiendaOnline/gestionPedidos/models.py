from django.db import models

# Create your models here.
#creando un modelo para la base de datos
#con esto creamos un estructura para nuestra base de datos inicial, debemos indicarle a django que tenemos una app nueva de gestion de pedidos entonces hacemos esto en settings.py

#creamos la base de datos con los modelos correspondientes que acabamos de definir en este archivo con el comando python3 manage.py makemigrations

#esto creara nuestra base de datos pero estara vacia

# -->python3 manage.py sqlmigrate gestionPedidos 0001 <--
#con este comando hacemos las migraciones de los modelos de la base de datos y introducimos las tablas dentro de esta, esto le da las intrucciones a django para que inserte el codigo sql automaticamente y inserte las tablas dentro de la base de datos

#el numero de migracion ayuda a verificar el numero de migraciones que hemos en la base de datos y los cambios que hemos hecho en ella

#python3 manage.py migrate con esto le decimos a python que utilice el codigo sql que acabamos de generar para finalmente tener las tablas dentro de la base de datos


class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    telefono=models.CharField(max_length=15)

#añandiendo cliente por consola python3 manage.py shell
# >>> from gestionPedidos.models import Clientes
# >>> cli=Clientes(nombre='kevin', direccion='mi casita', email='kevin.andresfontt@gmail.com', telefono='1234332223')
# >>> cli.save()

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()


#insertar registros from gestionPedidos.models import Articulos
#art=Articulos(nombre='MESA', seccion='decoracion', precio=90) creando un objeto para insertarlo en ta tabla si nos damos cuenta usamos las variables definidas en la clase articulo para construir el articulo segun su modelo en la base de datos
#art.save() ejecutar la consulta sql

#art3=Articulos.objects.create(nombre='TALADRO',#seccion='FERRETERIA', precio=65) metodo para agregar-insertar con un solo comando osea sin el .save()


#>>> art.precio=95
#>>> art.save() <--- operacion update, cambiado el precio del articulo


#>>> art5=Articulos.objects.get(id=3)   
#>>> art5.delete() <--- operacion delete borrando un articulo por su id


# >>> Lista=Articulos.objects.all()
# >>> Lista
# <QuerySet [<Articulos: Articulos object (1)>, <Articulos: Articulos object (2)>]>
# 
# >>> Lista.query.__str__()
# 'SELECT "gestionPedidos_articulos"."id", "gestionPedidos_articulos"."nombre", "gestionPedidos_articulos"."seccion", "gestionPedidos_articulos"."precio" FROM "gestionPedidos_articulos"'

#operacion select para la base de datos, que nos devuleve una lista con los articulos dentro de ella 



