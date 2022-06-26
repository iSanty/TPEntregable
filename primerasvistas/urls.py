from .views import inicio, ver_fecha, mi_template, saludo
from django.urls import path


urlpatterns = [
    path('', inicio),
    path('fecha/', ver_fecha),
    path('mi-template/', mi_template),
    path('saludo/<nombre>', saludo),
]
