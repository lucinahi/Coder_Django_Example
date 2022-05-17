from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Django - Coder")
def segundavista(request):
     return HttpResponse("Me debes un domingo")

def diaDeHoy(request):

        dia = datetime.today()

        documentoDeTexto = f"Hoy es día: <br> {dia}"

        return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre, edad):

      documentoDeTexto = f"Mi nombre es: {nombre} <br><br> Mi edad es: {edad}"

      return HttpResponse(documentoDeTexto)


def probandoTemplate(self):

    miHtml = open("/home/lucinahi/coder_python/Proyecto1/Proyecto1/Templates/template1.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)