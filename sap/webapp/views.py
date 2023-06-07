from django.http import HttpResponse
from django.template import loader
from personas.models import Personas

# Create your views here.
def bienvenido (request):
    #return HttpResponse("<!DOCTYPE html><html><head><title>APP</title></head><body><p>Hola Mundo desde Django</p></body></html>")
    pagina = loader.get_template("saludo.html")
    return HttpResponse(pagina.render())

def hola (request, nombre):
    apellido = request.GET["apellido"]
    nivel = request.GET["nivel"]
    curso = request.GET["curso"]
    pagina = loader.get_template("saludo.html")
    nombrecompleto =  nombre + " " + apellido
    datos ={"nombre": nombrecompleto , "curso":curso, "nivel":nivel}
    return HttpResponse(pagina.render(datos, request))

def edad (request, edad):
    pagina = loader.get_template("edad.html")
    mensaje = {"edad": edad}
    return HttpResponse(pagina.render(mensaje, request))


def mostrar_personas(request):
    cantidad_personas = Personas.objects.count()
    personas=Personas.objects.all().values()




    datos={"cantidad": cantidad_personas, "personas": personas,}
    pagina = loader.get_template("personas.html")
    return HttpResponse(pagina.render(datos, request))





