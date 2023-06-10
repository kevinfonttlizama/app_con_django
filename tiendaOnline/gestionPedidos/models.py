from django.db import models

# Create your models here.
#creando un modelo para la base de datos
#con esto creamos un estructura para nuestra base de datos inicial, debemos indicarle a django que tenemos una app nueva de gestion de pedidos entonces hacemos esto en settings.py

#creamos la base de datos con los modelos correspondientes que acabamos de definir en este archivo con el comando python3 manage.py makemigrations

#esto creara nuestra base de datos pero estara vacia

# -->python3 manage.py sqlmigrate gestionPedidos 0001 <--
#con este comando hacemos las migraciones de los modelos de la base de datos y introducimos las tablas dentro de esta, esto le da las intrucciones a django para que inserte el codigo sql automaticamente y inserte las tablas dentro de la base de datos

#el numero de migracion ayuda a verificar el numero de migraciones que hemos en la base de datos y los cambios que hemos hecho en ella


class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    telefono=models.CharField(max_length=15)


class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
