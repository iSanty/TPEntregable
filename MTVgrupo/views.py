from multiprocessing import context
from django.http import HttpResponse
from datetime import datetime

from django.template import Template, Context


def inicio(request):
    return HttpResponse('hola soy mi primer vista')

def mi_template(request):
    archivo = open(r'C:\Users\Santy1\Desktop\TpEntregable\templates\main.html', 'r')
    template_1 = Template(archivo.read())
    archivo.close()
    contexto1 = Context()
    
    render1 = template_1.render(contexto1)
    return HttpResponse(render1)
    
def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'fecha actual: {fecha_actual} ')