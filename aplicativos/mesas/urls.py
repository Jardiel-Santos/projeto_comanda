from django.contrib import admin
from django.urls import path, include
from aplicativos.mesas.views import mesas, index

urlpatterns = [
    path('', index),
    path('mesas', mesas, name= 'mesas')
]