from django.shortcuts import render

# importamos los modelos de tabla de la BDD
from .models import Especie,Mascota

# Create your views here.
def index(request):
    gatos = Mascota.objects.filter(nombre_especie='gato')
    perros = Mascota.objects.filter(nombre_especie='perro')
    especie = Especie.objects.all()
    contexto = {"gatos":gatos,"perros":perros, "especie":especie}

    return render(request,"index.html",contexto)

def consulta(request,id):
    mascota = Mascota.objects.filter(chip=id)
    contexto = {"mascota":mascota}
    return render(request,"consultar.html",contexto)

def ubicacion(request):
    return render(request,"ubicacion.html")