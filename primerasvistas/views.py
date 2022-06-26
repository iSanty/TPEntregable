
from django.http import HttpResponse
from datetime import datetime


from django.template import Template, Context, loader


def inicio(request):
    return HttpResponse('hola soy mi primer vista')



def mi_template(request):
    
    template1 = loader.get_template('main.html')

    nombre = 'momia'
    apellido = "Negra"
    render1 = template1.render({'nombre': nombre, 'apellido': apellido, 'edad':5500})
    return HttpResponse(render1)


    
def saludo(request, nombre):
    return HttpResponse(f'Hola : {nombre} ')
    
    
def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'fecha actual: {fecha_actual} ')