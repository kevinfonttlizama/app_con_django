"""
URL configuration for projectone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projectone.views import saludo, despedida,obtenerFecha, calculaEdad #<-- importamos la vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo', saludo), #<---añandiendo la url creandola y importando la vista creada en views
    path('adios', despedida),
    path('fecha', obtenerFecha),
    path('edades/<int:edad>/<int:year>',calculaEdad),#colocamos el caracter de angulares para dar parametros dentros de las url en este caso estamos dando dos parametros int para calcular la edades futuras, usando la funcion calculaEdad que creamos en el archivo de views.py que nos devuelve un calculo en una edas futura.


]
