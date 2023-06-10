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


#Importante siempre que hagamos cambios en los modelos debemos hacer las migraciones correspondientes. makemigrations - migrate

#el metodo __str__ lo que hace es convertir a una cadena de caracteres legible  
class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()

    def __str__(self):
        return 'EL nombre es %s la seccion es %s y el precio es %s'%(self.nombre,self.seccion,self.precio)


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
# >>> Lista <-- queda guardado en la variable lista
# y nos devuelve lo siguiente por consola
# <QuerySet [<Articulos: Articulos object (1)>, <Articulos: Articulos object (2)>]>
# con esto le pedimos que nos muestre lo que guardo dentro de la variable Lista que creamos y devuelve lo siguiente : 
# >>> Lista.query.__str__()
# 'SELECT "gestionPedidos_articulos"."id", "gestionPedidos_articulos"."nombre", "gestionPedidos_articulos"."seccion", "gestionPedidos_articulos"."precio" FROM "gestionPedidos_articulos"'

#operacion select para la base de datos, que nos devuleve una lista con los articulos dentro de ella 

#>>> python3 manage.py shell
#>>> from gestionPedidos.models import Articulos
#>>> Articulos.objects.filter(seccion='DEPORTES')
#esto nos devolveria todo lo que esta dentro de la seccion deportes filtrado
#<QuerySet []> me devuelve una lista vacia ya que no he introducido articulos en la base de datos 


# >>> Articulos.objects.filter(seccion='MUEBLES') <--- cuando le hacemos esta consulta a la base de datos por consola le decimos que nos filtre por la seccion muebles de la tabla articulos de la base de datos, si tenemos configurado el metodo __str__ nos devuelve la siguiente cadena por cada objeto que hayamos filtrado, en este caso el metodo __str__ nos devuelve la cadena --> return 'EL nombre es %s la seccion es %s y el precio es %s'%(self.nombre,self.seccion,self.precio) <--

#Entonces nos entrega esto por consola (lo de abajo)
#                         
# <QuerySet [<Articulos: EL nombre es SILLA la seccion es MUEBLES y el precio es 30>, <Articulos: EL nombre es MESA la seccion es MUEBLES y el precio es 80>, <Articulos: EL nombre es VELADOR la seccion es MUEBLES y el precio es 40>]>

#  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#            salida de la consola 
# 






