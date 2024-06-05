from django.contrib import admin
from django.urls import path, include
from aplicativos.mesas.views import mesas, index, mesa_numero

urlpatterns = [
    path('', index),
    path('mesas', mesas, name= 'mesas'),
    path('mesas/<int:mesa_id>', mesa_numero, name= 'mesa_numero'),
]